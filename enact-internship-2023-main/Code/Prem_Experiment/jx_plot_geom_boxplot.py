import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Read the CSV file into a DataFrame
df = pd.read_csv("jx_results/jx_process_level_methods.csv")

# Compute the mean of the "Total Energy (J)" column
mean_value = df["Total Energy (J)"].mean()
print("Mean value:", mean_value)

# Create a box plot with an average point and a stripplot
fig, ax = plt.subplots()
sns.boxplot(data=df, y="Total Energy (J)", showmeans=True, ax=ax)
sns.stripplot(data=df, y="Total Energy (J)", color=".3", ax=ax)
ax.axhline(mean_value, color="r", linestyle="--", label="Mean")
ax.set_xlabel("Total Energy (J)")
ax.set_ylabel("")
ax.set_title("Mandelbrot Java Program")
ax.legend()

# Check if the "jx_graphs" directory exists, and create it if it doesn't
if not os.path.exists("jx_graphs"):
    os.makedirs("jx_graphs")

# Save the plot to the "jx_graphs" directory
fig.savefig("jx_graphs/Mandelbrot_boxplot.png")

# Display the plot
plt.show()

