import pandas as pd

# Load dataset
df = pd.read_csv("data/mba_colleges.csv")

# Current salary before MBA
current_salary = 8

# Calculate salary increment
df["Salary_Increment"] = (
    df["Average_Package_LPA"] - current_salary
)

# ROI Percentage
df["ROI_Percent"] = (
    df["Salary_Increment"] /
    df["Fees_Lakhs"]
) * 100

print("\nMBA ROI Analysis\n")
print(df)

# Save results
df.to_csv(
    "outputs/mba_roi_results.csv",
    index=False
)

print("\nResults saved successfully!")
import matplotlib.pyplot as plt

# Sort by ROI
df_sorted = df.sort_values(
    by="ROI_Percent",
    ascending=False
)

plt.figure(figsize=(10,5))

plt.bar(
    df_sorted["College"],
    df_sorted["ROI_Percent"]
)

plt.title("MBA ROI Comparison")
plt.xlabel("College")
plt.ylabel("ROI (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/roi_comparison.png"
)

plt.show()