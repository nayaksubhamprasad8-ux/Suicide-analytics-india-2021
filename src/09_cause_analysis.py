import pandas as pd

df = pd.read_csv("Data/Cause-wise Distribution_2021.csv",encoding="cp1252")

# Show all causes
print("\nAll Causes:")
print(df[["Cause", "Total - Total"]])

# Top 10 causes
top_10 = df.sort_values("Total - Total",ascending=False).head(10)
print("\nTop 10 Causes:")
print(top_10[["Cause", "Total - Total"]])

# Bottom 10 causes
bottom_10 = df.sort_values("Total - Total",ascending=True).head(10)
print("\nBottom 10 Causes:")
print(bottom_10[["Cause", "Total - Total"]])

# Total recorded cases
print("\nTotal cases across causes:")
print(df["Total - Total"].sum())