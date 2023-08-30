# Power monitoring at the source code level using JoularJX

For doing the experiment we devided the task in two part:
- Power consumption monitoring of a single java program(mandelbrot.java) using JoularJX
- Power consumption monitoring of a project(cMath_original) using JoularJX

## Part-1

### Power consumption monitoring of a single java program(mandelbrot.java) using JoularJX.

### Description:

The first part of the experiment involves monitoring the power consumption of a single Java program, "mandelbrot.java," using JoularJX. The JoularJX 2.0 version was used to obtain updated tree structure results in the output directory. To execute the Java program with JoularJX, a script named "jx_script.sh" was created, which includes several Python files: "jx_gatherData.py," "jx_plot.py," "jx_process_level_methods.py," "shapiro_wilk_test_energy.py," and "shapiro_wilk_test_power.py."

The "jx_script.sh" script checks whether an argument is passed to it, and if not, it prints an error message and exits. It creates a "jx_results" directory and several subdirectories to store the results of the JoularJX performance analysis tool. The script runs the Java program multiple times with different parameters, specified in the for loop, and for each iteration, it runs the Java program with the JoularJX agent and redirects the output to either a file or /dev/null depending on whether it is the first iteration or not. The generated .pmb file is saved for the first iteration in the "mandelbrot_bitmap" directory, and the four files created by JoularJX, which contain the power and energy data for the Java program, are processed. The non-empty files are sorted and moved to their corresponding directories inside the "jx_results" directory, and the empty ones are deleted.

Finally, the script gathers, processes, plots, and performs statistical tests on the energy and power consumption data obtained using JoularJX.

### Installation:

1. Clone the repository: 
```
git clone https://gitlabev.imtbs-tsp.eu/sticamsud/enact-internship-2023.git
```
2. Navigate to the project directory: 
```
cd enact-internship-2023/Code/Prem_Experiment
```
3. Install JoularJX by following the instructions on their website:
```
 https://github.com/joular/joularjx
```
4. Compile the mandelbrot.java program: 

```
javac mandelbrot.java
```

### Usage:

- To execute the script we need to indicate the java class
```
./jx_script.sh mandelbrot
```

### Result

- Using JoularJX gathered power and energy consumption data  will save it to CSV file in the "jx_results" directory.
- Generate plots of the collected power and energy consumption data and save them to the "jx_graphs" directory.
- A folder "mandelbrot_bitmap" with figures in .pmb format
-  Analyze the power and energy consumption data at the method level and break it down into individual methods, calculating the energy and power consumed by each method.
- Perform a Shapiro-Wilk test on the energy consumption data to check for normality and found that the data was not normally distributed (p-value < 0.05).
- Perform a Shapiro-Wilk test on the power consumption data to check for normality and found that the data was not normally distributed (p-value < 0.05).


## Part-2

### Power consumption monitoring of a project(cMath_original) using JoularJX.

### Description:

The second part of the experiment involves monitoring the power consumption of a project called 'cMath_original' using JoularJX 2.0 to obtain updated tree structure results in the output directory. To execute all test cases of the project together, a new test class named 'RunAllSuite.java' was created in the test directory. To execute the 'RunAllSuite.java' class with JoularJX, it is necessary to download the 'cpsuite/cpsuite-1.2.6.jar.zip' file from the link 'http://www.java2s.com/Code/Jar/c/Downloadcpsuite126jar.htm' and unzip it. A script called 'jx_script_math.sh' in the 'cMath_original' directory is used to execute the 'RunAllSuite.java' class, which captures power and energy measurements using the JoularJX Java agent and manages the resulting files.

The script sets up directories for storing output files, sets the Java classpath, and runs the 'RunAllSuite.java' program in a loop for 30 iterations. During the first iteration, the output is saved to a file named 'java_temp.pmb,' and for subsequent iterations, the output is discarded. After running the Java program, the script searches for several output files created by the JoularJX Java agent and moves them to appropriate directories. Empty files are deleted.

Finally, the script gathers, processes, plots, and performs statistical tests on the energy and power consumption data obtained using JoularJX. The statistical tests are performed using several Python scripts, including 'jx_gatherData.py,' 'jx_plot.py,' 'jx_process_level_methods.py,' 'shapiro_wilk_test_energy.py,' and 'shapiro_wilk_test_power.py.'



### Installation:

1. Clone the repository: 

```
git clone https://gitlabev.imtbs-tsp.eu/sticamsud/enact-internship-2023.git
```

2. Navigate to the project directory: 

```
cd enact-internship-2023/Code/Prem_Experiment/cMath_original
```

3. Install JoularJX by following the instructions on their website:

```
 https://github.com/joular/joularjx
```

4. Navigate to the RunAllSuite.java file:

```
cd Code/Prem_Experiment/cMath_original/src/test/java
```

5. Compile the RunAllSuite.java file: 

```
javac -cp /home/tareq/cpsuite-1.2.6.jar:/usr/share/java/junit4.jar RunAllSuite.java
```

6. Move the compiled file(RunAllSuite.class) in the bin folder :

```
cd Code/Prem_Experiment/cMath_original/bin
```

### Usage:

- To execute the script we need to indicate the java class

```
./jx_script_math.sh 
```

Note: After running the command, if you face this error message "bash: ./jx_script_math.sh: Permission denied" use the given command below and after that re-run the previous command.

```
chmod +x jx_script_math.sh
```
### Result

- Using JoularJX gathered power and energy consumption data  will save it to CSV file in the "jx_results" directory.
- Generate plots of the collected power and energy consumption data and save them to the "jx_graphs" directory.
- A folder "mandelbrot_bitmap" with figures in .pmb format
-  Analyze the power and energy consumption data at the method level and break it down into individual methods, calculating the energy and power consumed by each method.
- Perform a Shapiro-Wilk test on the energy consumption data to check for normality and found that the data was not normally distributed (p-value < 0.05).
- Perform a Shapiro-Wilk test on the power consumption data to check for normality and found that the data was not normally distributed (p-value < 0.05).



## References

- [To run all tests in Junit 4 ](https://stackoverflow.com/questions/2255046/run-all-tests-in-junit-4).
- [cpsuite-1.2.6.jar](http://www.java2s.com/Code/Jar/c/Downloadcpsuite126jar.htm).
- [JoularJX](https://github.com/joular/joularjx).
- [Mandelbrot program](https://en.wikipedia.org/wiki/Mandelbrot_set).
- [To run a Java class in a package](https://stackoverflow.com/questions/11032590/how-do-i-run-a-java-class-in-a-package).




