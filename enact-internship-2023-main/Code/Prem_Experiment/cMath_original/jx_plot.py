import csv
import os
import matplotlib.pyplot as plt

# Read data from CSV file
with open('jx_results/jx_process_level_methods.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Extract iteration, total energy, and total power values
iterations = [int(row['Iteration']) for row in data]
total_energies = [float(row['Total Energy (J)']) for row in data]
total_powers = [float(row['Total Power (W)']) for row in data]

# Create figure for total energy
fig1 = plt.figure(figsize=(8, 5))

# Plot total energy vs iteration
plt.plot(iterations, total_energies, 'bo', label='Total Energy')
plt.xlabel('Iteration')
plt.ylabel('Total Energy (J)')
plt.legend()

# Save total energy graph to jx_graphs directory
if not os.path.exists('jx_graphs'):
    os.mkdir('jx_graphs')
fig1.savefig('jx_graphs/jx_total_energy.png', dpi=300)

# Clear figure
plt.clf()

# Create figure for total power
fig2 = plt.figure(figsize=(8, 5))

# Plot total power vs iteration
plt.plot(iterations, total_powers, 'ro', label='Total Power')
plt.xlabel('Iteration')
plt.ylabel('Total Power (W)')
plt.legend()

# Save total power graph to jx_graphs directory
fig2.savefig('jx_graphs/jx_total_power.png', dpi=300)

# Display figures
plt.show()
