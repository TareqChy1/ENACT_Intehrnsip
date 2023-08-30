import csv

# Read data from the provided CSV
with open('jx_results/joularJX_calltrees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    data = list(reader)

# Create dictionaries to store results for each iteration
total_energy = {}
avg_energy = {}
total_power = {}
avg_power = {}
sample_count = {}

# Calculate total and average energy consumption, and total and average power consumption for each iteration
for row in data:
    if len(row) >= 5:  # Check if row has enough columns
        iteration = row[2]
        energy = float(row[3]) if row[3] != '' else 0.0
        power = float(row[4]) if row[4] != '' else 0.0

        if iteration not in total_energy:
            total_energy[iteration] = 0.0
            avg_energy[iteration] = 0.0
            total_power[iteration] = 0.0
            avg_power[iteration] = 0.0
            sample_count[iteration] = 0

        total_energy[iteration] += energy
        total_power[iteration] += power
        sample_count[iteration] += 1

# Calculate average values
for iteration in total_energy:
    if sample_count[iteration] != 0:
        avg_energy[iteration] = total_energy[iteration] / sample_count[iteration]
        avg_power[iteration] = total_power[iteration] / sample_count[iteration]
    else:
        avg_energy[iteration] = 0.0
        avg_power[iteration] = 0.0

# Write results to a new CSV file
with open('jx_results/jx_process_level_calltrees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Iteration', 'Total Energy (J)', 'Average Energy (J)', 'Total Power (W)', 'Average Power (W)'])
    for iteration in total_energy:
        writer.writerow([iteration, total_energy[iteration], avg_energy[iteration], total_power[iteration], avg_power[iteration]])

print("Results have been written to 'jx_results/jx_process_level_calltrees.csv' file.")

