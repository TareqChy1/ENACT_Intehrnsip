import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon
from scipy import stats
from scipy.stats import t

# Step 1: Load the data from the original and optimized triangle files
original_file_path = "triangle_original/jx_results/jx_process_level_methods.csv"
optimized_file_path = "triangle_optimised/jx_results/jx_process_level_methods.csv"

original_data = pd.read_csv(original_file_path)
optimized_data = pd.read_csv(optimized_file_path)

# Step 2: Calculate the Wilcoxon test and statistical confidence percent
energy_original = original_data["Total Energy (J)"]
energy_optimized = optimized_data["Total Energy (J)"]
power_original = original_data["Total Power (W)"]
power_optimized = optimized_data["Total Power (W)"]

wilcoxon_energy, p_value_energy = wilcoxon(energy_original, energy_optimized)
wilcoxon_power, p_value_power = wilcoxon(power_original, power_optimized)

alpha = 0.05  # Or any other significance level you prefer

# print the Wilcoxon statistics and p-values
print("Wilcoxon statistic for Energy:", wilcoxon_energy)
print("P-value for Energy:", p_value_energy)
print("Wilcoxon statistic for Power:", wilcoxon_power)
print("P-value for Power:", p_value_power)


# Calculate and print average and standard deviation for total energy
energy_original_mean = energy_original.mean()
energy_optimized_mean = energy_optimized.mean()
energy_original_std = energy_original.std()
energy_optimized_std = energy_optimized.std()

# Calculate the standard error for original and optimized
energy_original_se = energy_original_std / np.sqrt(len(energy_original))
energy_optimized_se = energy_optimized_std / np.sqrt(len(energy_optimized))

# Calculate the confidence interval for a 95% confidence level for both original and optimized
confidence_level = 0.95
degrees_freedom_original = len(energy_original) - 1
degrees_freedom_optimized = len(energy_optimized) - 1
confidence_interval_original = t.interval(confidence_level, degrees_freedom_original, energy_original_mean, energy_original_se)
confidence_interval_optimized = t.interval(confidence_level, degrees_freedom_optimized, energy_optimized_mean, energy_optimized_se)

# Calculate the percentage of error relative to the mean for both original and optimized
margin_of_error_original = (confidence_interval_original[1] - confidence_interval_original[0]) / 2
margin_of_error_optimized = (confidence_interval_optimized[1] - confidence_interval_optimized[0]) / 2
percentage_error_original = (margin_of_error_original / energy_original_mean) * 100
percentage_error_optimized = (margin_of_error_optimized / energy_optimized_mean) * 100

print("Original Triangle Total Energy Mean:", energy_original_mean)
print("Original Triangle Total Energy Std Deviation:", energy_original_std)
print("95% Confidence Interval for Original Triangle Total Energy Mean:", confidence_interval_original)
# print("Percentage of Error for Original Triangle Total Energy Mean:", percentage_error_original)
print("Percentage of Error for Original Triangle Total Energy Mean:", percentage_error_original, "%")

print("Optimized Triangle Total Energy Mean:", energy_optimized_mean)
print("Optimized Triangle Total Energy Std Deviation:", energy_optimized_std)
print("95% Confidence Interval for Optimized Triangle Total Energy Mean:", confidence_interval_optimized)
#print("Percentage of Error for Optimized Triangle Total Energy Mean:", percentage_error_optimized)
print("Percentage of Error for Optimized Triangle Total Energy Mean:", percentage_error_optimized, "%")



# Compare means and print message for energy consumption

if energy_original_mean > energy_optimized_mean:
    print("The original version consumes more energy than the optimized version.")
else:
    print("The optimized version consumes more energy than the original version.")

# Same process for power consumption
power_original_mean = power_original.mean()
power_optimized_mean = power_optimized.mean()

if power_original_mean > power_optimized_mean:
    print("The original version consumes more power than the optimized version.")
else:
    print("The optimized version consumes more power than the original version.")

# Step 3: Create a histogram for total energy consumption
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.hist(original_data["Iteration"], bins=80, weights=original_data["Total Energy (J)"], alpha=1, label=f"Original Triangle")
plt.hist(optimized_data["Iteration"], bins=80, weights=optimized_data["Total Energy (J)"], alpha=1, label=f"Optimized Triangle")
plt.xlabel("Process ID")
plt.ylabel("Total Energy (J)")
plt.title('Comparison of Total Energy Consumption')
# Adjust the position of the legend inside the plot, centered at the top
plt.legend(prop={'size': 5}, loc='upper center', bbox_to_anchor=(0.5, 0.95), fancybox=True)

# Step 4: Create a histogram for total power consumption
plt.subplot(1, 2, 2)
plt.hist(original_data["Iteration"], bins=80, weights=original_data["Total Power (W)"], alpha=1, label=f"Original Triangle")
plt.hist(optimized_data["Iteration"], bins=80, weights=optimized_data["Total Power (W)"], alpha=1, label=f"Optimized Triangle")
plt.xlabel("Process ID")
plt.ylabel("Total Power (W)")
plt.title('Comparison of Total Power Consumption')
# Adjust the position of the legend inside the plot, centered at the top
plt.legend(prop={'size': 5}, loc='upper center', bbox_to_anchor=(0.5, 0.95), fancybox=True)

plt.tight_layout()
plt.savefig('plots/histograms.png')  # Save histograms to 'histograms.png'
plt.close()

# Step 5: Create box plots for total energy and power consumption
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.boxplot(data=[energy_original, energy_optimized])
plt.xticks([0, 1], ['Original', 'Optimized'])
plt.xlabel('Triangle Program')
plt.ylabel('Total Energy (J)')
plt.title('Comparison of Total Energy Consumption')

plt.subplot(1, 2, 2)
sns.boxplot(data=[power_original, power_optimized])
plt.xticks([0, 1], ['Original', 'Optimized'])
plt.xlabel('Triangle Program')
plt.ylabel('Total Power (W)')
plt.title('Comparison of Total Power Consumption')

plt.tight_layout()
plt.savefig('plots/boxplots.png')  # Save the box plots to 'boxplots.png'
plt.close()

