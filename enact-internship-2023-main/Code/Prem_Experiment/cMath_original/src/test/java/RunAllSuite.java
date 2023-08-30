import org.junit.extensions.cpsuite.ClasspathSuite;
import org.junit.extensions.cpsuite.ClasspathSuite.*;
import org.junit.internal.TextListener;
import org.junit.runner.RunWith;
import org.junit.runner.JUnitCore;
import static org.junit.extensions.cpsuite.SuiteType.*;

@RunWith(ClasspathSuite.class)
@SuiteTypes({ JUNIT38_TEST_CLASSES, TEST_CLASSES })
public class RunAllSuite {
        /* main method not needed, but I use it to run the tests */
        public static void main(String args[]) {
            //JUnitCore.runClasses(RunAllSuite.class);
        	JUnitCore junit = new JUnitCore();
            junit.addListener(new TextListener(System.out));
            junit.run(RunAllSuite.class);
        }
}