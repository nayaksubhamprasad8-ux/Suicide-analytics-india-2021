import pandas as pd

df = pd.read_csv("Data/Cause-wise Distribution_mode_2021.csv",encoding="cp1252")

# Show all modes
print("\nAll Modes:")
print(df[["Cause", "Total"]])

# Top 10 modes
top_10 = df.sort_values("Total",ascending=False).head(10)
print("\nTop 10 Modes:")
print(top_10[["Cause", "Total"]])

# Percentage share
print("\nPercentage Share:")
print(top_10[["Cause", "Total", "Percentage Share"]])

# Total cases
print("\nTotal cases across modes:")
print(df["Total"].sum())