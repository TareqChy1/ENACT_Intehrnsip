#!/bin/bash

jar="/opt/joularjx/joularjx-2.0.jar"

mkdir -p "jx_results/energy/methods" "jx_results/energy/calltrees" \
         "jx_results/energy_filtered/methods" "jx_results/energy_filtered/calltrees" \
         "jx_results/power/methods" "jx_results/power/calltrees" \
         "jx_results/power_filtered/methods" "jx_results/power_filtered/calltrees" \
         "cMath_original_bitmap"



export CLASSPATH=/home/tareq/Documents/enact-internship-2023/Code/Prem_Experiment/cMath_original/bin:/home/tareq/cpsuite-1.2.6.jar:/usr/share/java/junit4.jar 

for i in {1..30}; do
    echo "running iteration $i"
    # We need the PID of the java process to manage the files created by JoularJX correctly
    if [ $i == 1 ]; then
        java -javaagent:$jar -cp $CLASSPATH RunAllSuite > "cMath_original_bitmap/java_temp.pmb" &
    else
        java -javaagent:$jar -cp $CLASSPATH RunAllSuite > /dev/null 2>/dev/null &
    fi
    
    java_pid=$!
    wait $!


    # Four files created
    fichier_energy_methods="joularJX-$java_pid-all-methods-energy.csv"
    fichier_energy_calltrees="joularJX-$java_pid-all-call-trees-energy.csv"
    fichier_energy_filtered_methods="joularJX-$java_pid-filtered-methods-energy.csv"
    fichier_energy_filtered_calltrees="joularJX-$java_pid-filtered-call-trees-energy.csv"
    
    fichier_power_methods="joularJX-$java_pid-all-methods-power.csv"
    fichier_power_calltrees="joularJX-$java_pid-all-call-trees-power.csv"
    fichier_power_filtered_methods="joularJX-$java_pid-filtered-methods-power.csv"
    fichier_power_filtered_calltrees="joularJX-$java_pid-filtered-call-trees-power.csv"

    # Sort empty files
    find . -name "$fichier_energy_methods" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/energy/methods"
            #echo "Moved $f to jx_results/energy/methods"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
    
    find . -name "$fichier_energy_calltrees" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/energy/calltrees"
            #echo "Moved $f to jx_results/energy/calltrees"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
 
    find . -name "$fichier_energy_filtered_methods" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/energy_filtered/methods"
            #echo "Moved $f to jx_results/energy_filtered/methods"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
    find . -name "$fichier_energy_filtered_calltrees" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/energy_filtered/calltrees"
            #echo "Moved $f to jx_results/energy_filtered/calltrees"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
    find . -name "$fichier_power_methods" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/power/methods"
            #echo "Moved $f to jx_results/power/methods"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
    find . -name "$fichier_power_calltrees" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/power/calltrees"
            #echo "Moved $f to jx_results/power/calltrees"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
    find . -name "$fichier_power_filtered_methods" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/power_filtered/methods"
            #echo "Moved $f to jx_results/power_filtered/methods"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done
    find . -name "$fichier_power_filtered_calltrees" -type f -print0 | while IFS= read -r -d '' f; do
        if [ -s "$f" ]; then
            # Non-empty file
            mv "$f" "jx_results/power_filtered/calltrees"
            #echo "Moved $f to jx_results/power_filtered/calltrees"
        else
            # Empty file
            #echo "Deleting empty file: $f"
            rm -f "$f"
        fi
    done	
done

trap "trap - SIGTERM && kill -- -$$ > /dev/null 2>&1" SIGINT SIGTERM EXIT # Au cas où

# used to gather power and engery consumption data using JoularJX and save it t CSV file.
python3 jx_gatherData.py "jx_results/"

#used to analyze the power consumption data at the method level, i.e., it breaks down the data into individual methods and calculates the energy and power consumed by each method.
python3 jx_process_level_methods.py "jx_results/"

# used to generate graphs from the power and engery consumption data saved in the CSV file generated by jx_gatherData.py.
python3 jx_plot.py  "jx_graphs"

# for box plotting the total energy for all the process id
python3 jx_plot_geom_boxplot.py

#used to perform a Shapiro-Wilk test on the energy consumption data to check for normality.
python3 shapiro_wilk_test_energy.py

#used to perform a Shapiro-Wilk test on the power consumption data to check for normality.
python3 shapiro_wilk_test_power.py
