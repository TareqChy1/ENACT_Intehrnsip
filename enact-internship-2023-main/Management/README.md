The experiment described involves monitoring the power consumption of a single Java program, specifically the "mandelbrot.java" program, using JoularJX, a performance analysis tool. The JoularJX version 2.0 is used, and several Python files are included like 
"jx_gatherData.py", "jx_plot.py", "jx_process_level_methods.py", "shapiro_wilk_test_energy.py" and "shapiro_wilk_test_power.py" in a script named "jx_script.sh" to execute the program with JoularJX. 

The program "jx_gatherData.py" reads energy and power data from CSV files in specific directories, and creates Pandas dataframes to store the data. The dataframes are then processed to extract relevant information (such as method names, parameters, iterations, and energy/power consumption), and this information is stored in lists. The lists are then used to create new dataframes with meaningful column names, which are then saved to CSV files.

More specifically, the code does the following:
- Imports necessary Python libraries: math, os, numpy, pandas, matplotlib, and sys.
- Reads in a folder name as a command line argument using sys.argv.
- Creates empty lists to store data for the energy and power consumption of different methods.
- Collects the paths to CSV files containing energy data for each method in the "./dossier_result/energy/methods" directory. For each file, the method name, parameter, iteration number, and energy consumption are extracted and stored in the appropriate lists.
- Creates a Pandas dataframe to store the energy consumption data, with columns for method name, parameter, iteration number, and energy consumption.
- Collects the paths to CSV files containing energy data for each method in the "./dossier_result/energy/calltrees" directory. For each file, the method name, parameter, iteration number, and energy consumption are extracted and stored in the appropriate lists.
- Creates a second Pandas dataframe to store the energy consumption data from call trees, with columns for method name, parameter, iteration number, and energy consumption.
- Collects the paths to CSV files containing power data for each method in the "./dossier_result/power/methods" directory. For each file, the method name, parameter, iteration number, and power consumption are extracted and stored in the appropriate lists.
- Creates a third Pandas dataframe to store the power consumption data, with columns for method name, parameter, iteration number, and power consumption.
- Clears the lists that were used to store the data.
- The resulting dataframes are then saved to CSV files with appropriate names.


The "jx_plot.py" program does the data visualization using Python libraries such as NumPy, Pandas, and Matplotlib to plot graphs from a CSV file. The code reads a CSV file with a specific header format and extracts data to plot two types of graphs: power consumption and energy consumption. The graphs display the impact of the number of elements on power and energy consumption, and the different methods used are represented by different colors on the graph. The code also creates a directory and saves the generated graphs in the given directory.

The "jx_process_level_methods.py" program reads data from a CSV file containing energy and power consumption values for different iterations of a process. It then calculates the total and average energy consumption, and total and average power consumption for each iteration, and writes these results to a new CSV file. The code uses the Python CSV module to read and write CSV files, and stores the results in dictionaries.


"shapiro_wilk_test_energy.py" and "shapiro_wilk_test_power.py" programs use the Pandas and Scipy libraries to perform a Shapiro-Wilk test for normality on a specific column of a CSV file. First, the CSV file is read using Pandas' read_csv function and the column of interest is extracted and stored in the variable column_data. Then, the Shapiro-Wilk test is performed on this column using Scipy's shapiro function, which returns the test statistic and p-value. The test statistic and p-value are then printed using print statements. The code then sets a significance level of 0.05 and compares the p-value with this level to determine whether to reject the null hypothesis that the data follows a normal distribution. If the p-value is greater than the significance level, the code prints a message indicating that the data follows a normal distribution; otherwise, it prints a message indicating that the data does not follow a normal distribution.


The script creates a "jx_results" directory and several subdirectories to store the results of the analysis tool. The Java program is executed multiple times with different parameters, and for each iteration, it is run with the JoularJX agent, and the output is redirected to a file or /dev/null. The generated .pmb file is saved for the first iteration, and the four files created by JoularJX, which contain the power and energy data, are processed. The non-empty files are sorted and moved to their corresponding directories inside the "jx_results" directory, and the empty ones are deleted. The script then gathers, processes, plots, and performs statistical tests on the energy and power consumption data obtained using JoularJX.

To use the script, the user needs to clone the repository, navigate to the project directory, install JoularJX following the instructions on their website, and compile the mandelbrot.java program. To execute the script, the user needs to indicate the java class by running the command "./jx_script.sh mandelbrot" in the terminal.

The result of the experiment is that the power and energy consumption data are saved to a CSV file in the "jx_results" directory, and plots of the collected data are generated and saved to the "jx_graphs" directory. A folder named "mandelbrot_bitmap" is also created, containing figures in .pmb format. The power and energy consumption data are analyzed at the method level, and the energy and power consumed by each method are calculated. A Shapiro-Wilk test is performed on the energy and power consumption data to check for normality, and it is found that the data was normally distributed (p-value > 0.05).
