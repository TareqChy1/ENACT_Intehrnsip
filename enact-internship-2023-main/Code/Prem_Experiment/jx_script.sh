#!/bin/bash

if [ "$#" -ne 1 ];then
    echo "Un unique argument est attendu : le nom du programme (sans l'extension)" >&2
    exit 1
fi

programme=$1
jar="/opt/joularjx/joularjx-2.0.jar"
mkdir "jx_results"

mkdir "jx_results/energy"
mkdir "jx_results/energy/methods"
mkdir "jx_results/energy/calltrees"

mkdir "jx_results/energy_filtered"
mkdir "jx_results/energy_filtered/methods"
mkdir "jx_results/energy_filtered/calltrees"

mkdir "jx_results/power"
mkdir "jx_results/power/methods"
mkdir "jx_results/power/calltrees"

mkdir "jx_results/power_filtered"
mkdir "jx_results/power_filtered/methods"
mkdir "jx_results/power_filtered/calltrees"

mkdir "mandelbrot_bitmap"



for param in 15000 20000 30000 40000 # Nombre d'élements dans un tableau
do    
    #for i in 1 2  # Nombre d'itérations
    for i in {1..30}  # Nombre d'itérations
    do 
	echo "running java  with parameter $param, iteration $i"
	# Nous avons besoin du pid du processus java pour pouvoir correctement gérer les fichiers créés par JoularJX
	if [ $i == 1 ];then
	    # On sauvegarde les pmb pour la première itération
	    
	    java -javaagent:$jar $programme $param > "mandelbrot_bitmap/java_temp.pmb" &
	    
	else
	    java -javaagent:$jar $programme $param > /dev/null 2>/dev/null &
	fi
	java_pid=$!
	wait $!

	# Sauvegarde du pmb
	if [ -e "mandelbrot_bitmap/java_temp.pmb" ];then
	    tail -n+6 "mandelbrot_bitmap/java_temp.pmb" > "mandelbrot_bitmap/java_$param.pmb"
	    rm -f "mandelbrot_bitmap/java_temp.pmb"
	fi
	
	# 4 fichiers créés
	fichier_energy_methods="joularJX-"$java_pid"-all-methods-energy.csv"
	fichier_energy_calltrees="joularJX-"$java_pid"-all-call-trees-energy.csv"
	fichier_energy_filtered_methods="joularJX-"$java_pid"-filtered-methods-energy.csv"
	fichier_energy_filtered_calltrees="joularJX-"$java_pid"-filtered-call-trees-energy.csv"
	
	fichier_power_methods="joularJX-"$java_pid"-all-methods-power.csv"
	fichier_power_calltrees="joularJX-"$java_pid"-all-call-trees-power.csv"
	fichier_power_filtered_methods="joularJX-"$java_pid"-filtered-methods-power.csv"
	fichier_power_filtered_calltrees="joularJX-"$java_pid"-filtered-call-trees-power.csv"


	# Tri des fichiers vides
	find . -name "$fichier_energy_methods" -type f -print0 | while IFS= read -r -d '' f
	do
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


	find . -name "$fichier_energy_calltrees" -type f -print0 | while IFS= read -r -d '' f
	do
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
	
	
	find . -name "$fichier_energy_filtered_methods" -type f -print0 | while IFS= read -r -d '' f
	do
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
	
	
	find . -name "$fichier_energy_filtered_calltrees" -type f -print0 | while IFS= read -r -d '' f
	do
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
	
	find . -name "$fichier_power_methods" -type f -print0 | while IFS= read -r -d '' f
	do
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
	
	find . -name "$fichier_power_calltrees" -type f -print0 | while IFS= read -r -d '' f
	do
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

	find . -name "$fichier_power_filtered_methods" -type f -print0 | while IFS= read -r -d '' f
	do
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
	
	find . -name "$fichier_power_filtered_calltrees" -type f -print0 | while IFS= read -r -d '' f
	do
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
