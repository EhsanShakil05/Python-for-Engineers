# Engineering Data Analysis with Python

# Read csv

import pandas as pd

data = pd.read_csv("C:\\Users\\HP\\OneDrive - National University of Sciences & Technology\\Summer 2026\\Python\\Data Analysis\\beam_test.csv")

print(data)

# Basic Statistics

print(data.describe())

# Engineering Analysis
# Maximum Deflection

max_def = data["Deflection"].max()

print(max_def)

# Average Deflection

avg_def = data["Deflection"].mean()

print(avg_def)

# Plotting Experimental Data

import matplotlib.pyplot as plt

plt.plot(
    data["Load"],
    data["Deflection"],
    marker="o"
)

plt.title("Load vs Deflection")

plt.xlabel("Load (N)")
plt.ylabel("Deflection (mm)")

plt.grid(True)

plt.show()

# Export Results

results = {
    "Average Deflection (mm)": [avg_def],

    "Maximum Deflection (mm)": [max_def]
}

summary = pd.DataFrame(results)

summary.to_csv("C:\\Users\\HP\\OneDrive - National University of Sciences & Technology\\Summer 2026\\Python\\Data Analysis\\beam_test_summary.csv", index=False)
