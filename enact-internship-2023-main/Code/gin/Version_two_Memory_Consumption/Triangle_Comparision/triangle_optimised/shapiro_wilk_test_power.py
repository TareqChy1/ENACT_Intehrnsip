import pandas as pd
from scipy.stats import shapiro

# Read CSV file
data = pd.read_csv("jx_results/jx_process_level_methods.csv")

# Extract the column of interest
column_data = data["Total Power (W)"]

# Perform Shapiro-Wilk test
statistic, p_value = shapiro(column_data)

# Print the test statistic and p-value
print("\n\n------ Shapiro-Wilk Test Results for Power for Triangle(Optimised) ------")
print("Test Statistic:", statistic)
print("P-value:", p_value)

# Set significance level
alpha = 0.05

# Compare p-value with significance level
if p_value > alpha:
    print("The data follows a normal distribution (fail to reject null hypothesis)")
else:
    print("The data does not follow a normal distribution (reject null hypothesis)")

