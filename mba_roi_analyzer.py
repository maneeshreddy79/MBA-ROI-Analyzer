import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/mba_colleges.csv")

# User Inputs
current_salary = float(
    input("Enter your current salary (LPA): ")
)

annual_growth = float(
    input("Expected annual salary growth (%): ")
)

# Function for Future Salary Projection
def future_salary(
    salary,
    growth_rate,
    years
):
    return salary * ((1 + growth_rate / 100) ** years)

# Salary Projection Without MBA
salary_after_5_years = future_salary(
    current_salary,
    annual_growth,
    5
)

print(
    "\nProjected Salary After 5 Years:",
    round(salary_after_5_years, 2),
    "LPA"
)

# ROI Calculations
df["Salary_Increment"] = (
    df["Average_Package_LPA"] - current_salary
)

df["ROI_Percent"] = (
    df["Salary_Increment"] /
    df["Fees_Lakhs"]
) * 100

df["Payback_Years"] = (
    df["Fees_Lakhs"] /
    df["Salary_Increment"]
)

print("\nMBA ROI Analysis\n")
print(df)

# Save Results
df.to_csv(
    "outputs/mba_roi_results.csv",
    index=False
)

print("\nResults saved successfully!")

# ROI Comparison Chart
df_sorted = df.sort_values(
    by="ROI_Percent",
    ascending=False
)

plt.figure(figsize=(10, 5))

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

# MBA Salary Projection
mba_salary = df["Average_Package_LPA"].mean()

mba_salary_after_5_years = future_salary(
    mba_salary,
    annual_growth,
    5
)

print(
    "\nAverage MBA Salary After 5 Years:",
    round(mba_salary_after_5_years, 2),
    "LPA"
)

difference = (
    mba_salary_after_5_years -
    salary_after_5_years
)

print(
    "\nMBA Advantage After 5 Years:",
    round(difference, 2),
    "LPA"
)

# MBA vs Non-MBA Chart
comparison = {
    "Without MBA": salary_after_5_years,
    "With MBA": mba_salary_after_5_years
}

plt.figure(figsize=(6, 4))

plt.bar(
    comparison.keys(),
    comparison.values()
)

plt.title(
    "MBA vs Non-MBA Salary After 5 Years"
)

plt.ylabel("Salary (LPA)")

plt.tight_layout()

plt.savefig(
    "outputs/mba_vs_non_mba.png"
)

plt.show()

# Top ROI Colleges
top_colleges = df.sort_values(
    by="ROI_Percent",
    ascending=False
)

print("\nTop 3 MBA Colleges Based On ROI\n")

print(
    top_colleges[
        ["College", "ROI_Percent"]
    ].head(3)
)

# Top Payback Colleges
top_payback = df.sort_values(
    by="Payback_Years"
)

print("\nTop 3 Colleges Based On Payback Period\n")

print(
    top_payback[
        ["College", "Payback_Years"]
    ].head(3)
)

# Key Insight
best_roi = df.loc[
    df["ROI_Percent"].idxmax()
]

print("\nKey Insight")

print(
    f"{best_roi['College']} provides the highest ROI of {best_roi['ROI_Percent']:.2f}%"
)

# Save Insights
with open(
    "outputs/project_insights.txt",
    "w"
) as file:

    file.write(
        f"Best ROI College: {best_roi['College']}\n"
    )

    file.write(
        f"ROI: {best_roi['ROI_Percent']:.2f}%\n"
    )

print("\nInsights saved successfully!")