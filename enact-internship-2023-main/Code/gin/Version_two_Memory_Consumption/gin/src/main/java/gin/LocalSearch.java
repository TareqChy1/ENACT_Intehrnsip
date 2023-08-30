package gin;

import com.sampullara.cli.Args;
import com.sampullara.cli.Argument;
import gin.edit.Edit;
import gin.edit.Edit.EditType;
import gin.test.InternalTestRunner;
import gin.test.UnitTestResult;
import gin.test.UnitTestResultSet;
import org.apache.commons.io.FilenameUtils;
import org.apache.commons.rng.simple.JDKRandomBridge;
import org.apache.commons.rng.simple.RandomSource;
import org.pmw.tinylog.Logger;

import java.io.File;
import java.io.Serial;
import java.io.Serializable;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * Simple local search. Takes a source filename and a method signature, optimizes it.
 * Assumes the existence of accompanying Test Class.
 * The class must be in the top level package if classPath not provided.
 */
public class LocalSearch implements Serializable {

    @Serial
    private static final long serialVersionUID = -92020344633720482L;

    private static final int WARMUP_REPS = 10;

    @Argument(alias = "f", description = "Required: Source filename", required = true)
    protected File filename = null;

    @Argument(alias = "m", description = "Required: Method signature including arguments." +
            "For example, \"classifyTriangle(int,int,int)\"", required = true)
    protected String methodSignature = "";

    @Argument(alias = "s", description = "Seed")
    protected Integer seed = 123;

    @Argument(alias = "n", description = "Number of steps")
    protected Integer numSteps = 100;

    @Argument(alias = "d", description = "Top directory")
    protected File packageDir;

    @Argument(alias = "c", description = "Class name")
    protected String className;

    @Argument(alias = "cp", description = "Classpath")
    protected String classPath;

    @Argument(alias = "t", description = "Test class name")
    protected String testClassName;

    @Argument(alias = "et", description = "Edit type: this can be a member of the EditType enum (LINE,STATEMENT,MATCHED_STATEMENT,MODIFY_STATEMENT); the fully qualified name of a class that extends gin.edit.Edit, or a comma-separated list of both")
    protected String editType = EditType.LINE.toString();

    /**
     * allowed edit types for sampling: parsed from editType
     */
    protected List<Class<? extends Edit>> editTypes;

    @Argument(alias = "ff", description = "Fail fast. "
            + "If set to true, the tests will stop at the first failure and the next patch will be executed. "
            + "You probably don't want to set this to true for Automatic Program Repair.")
    protected Boolean failFast = false;

    protected SourceFile sourceFile;
    protected Random rng;
    InternalTestRunner testRunner;

    // Constructor parses arguments
    LocalSearch(String[] args) {
        Args.parseOrExit(this, args);
        editTypes = Edit.parseEditClassesFromString(editType);

        this.sourceFile = SourceFile.makeSourceFileForEditTypes(editTypes, this.filename.toString(), Collections.singletonList(this.methodSignature));

        this.rng = new JDKRandomBridge(RandomSource.MT, Long.valueOf(seed));
        if (this.packageDir == null) {
            this.packageDir = (this.filename.getParentFile() != null) ? this.filename.getParentFile().getAbsoluteFile() : new File(System.getProperty("user.dir"));
        }
        if (this.classPath == null) {
            this.classPath = this.packageDir.getAbsolutePath();
        }
        if (this.className == null) {
            this.className = FilenameUtils.removeExtension(this.filename.getName());
        }
        if (this.testClassName == null) {
            this.testClassName = this.className + "Test";
        }
        this.testRunner = new InternalTestRunner(className, classPath, testClassName, failFast);
    }

    // Instantiate a class and call search
    public static void main(String[] args) {
        LocalSearch simpleLocalSearch = new LocalSearch(args);
        simpleLocalSearch.search();
    }

    // Apply empty patch and return memory consumption
    private long memoryOriginalCode() {
        Patch emptyPatch = new Patch(this.sourceFile);
        UnitTestResultSet resultSet = testRunner.runTests(emptyPatch, WARMUP_REPS);

        if (!resultSet.allTestsSuccessful()) {
            if (!resultSet.getCleanCompile()) {
                Logger.error("Original code failed to compile");
            } else {
                Logger.error("Original code failed to pass unit tests");
                for (UnitTestResult testResult : resultSet.getResults()) {
                    Logger.error(testResult);
                }
            }
            System.exit(0);
        }

        return resultSet.totalMemoryUsage() / WARMUP_REPS;
    }

    // Simple local search
    private void search() {
        Logger.info(String.format("Localsearch on file: %s method: %s", filename, methodSignature));

        // Memory consumption of original code
        long origMemory = memoryOriginalCode();
        Logger.info("Original memory consumption: " + origMemory + " Mbytes");

        // Start with empty patch
        Patch bestPatch = new Patch(this.sourceFile);
        long bestMemory = origMemory;

        for (int step = 1; step <= numSteps; step++) {
            Patch neighbour = neighbour(bestPatch);
            UnitTestResultSet testResultSet = testRunner.runTests(neighbour, 1);

            String msg;

            if (!testResultSet.getValidPatch()) {
                msg = "Patch invalid";
            } else if (!testResultSet.getCleanCompile()) {
                msg = "Failed to compile";
            } else if (!testResultSet.allTestsSuccessful()) {
                msg = "Failed to pass all tests";
            } else if (testResultSet.totalMemoryUsage() >= bestMemory) {
                msg = "Memory: " + testResultSet.totalMemoryUsage() + " Mbytes";
            } else {
                bestPatch = neighbour;
                bestMemory = testResultSet.totalMemoryUsage();
                msg = "New best memory consumption: " + bestMemory + " Mbytes ";
            }

            Logger.info(String.format("Step: %d, Patch: %s, %s ", step, neighbour, msg));
        }

        Logger.info(String.format("Finished. Best memory consumption: %d Mbytes, Memory reduction: %.2f%%, Patch: %s",
                bestMemory,
                100.0 * ((origMemory - bestMemory) / (1.0 * origMemory)),
                bestPatch));

        bestPatch.writePatchedSourceToFile(sourceFile.getRelativePathToWorkingDir() + ".optimised");
    }

    /**
     * Generate a neighboring patch, either by deleting an edit or adding a new one.
     *
     * @param patch Generate a neighbor of this patch.
     * @return A neighboring patch.
     */
    Patch neighbour(Patch patch) {
        Patch neighbour = patch.clone();

        if (neighbour.size() > 0 && rng.nextFloat() > 0.5) {
            neighbour.remove(rng.nextInt(neighbour.size()));
        } else {
            neighbour.addRandomEditOfClasses(rng, editTypes);
        }

        return neighbour;
    }
}
