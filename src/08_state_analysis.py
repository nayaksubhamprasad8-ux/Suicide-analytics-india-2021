import pandas as pd

df = pd.read_csv("Data/master_state_dataset_2021.csv")

# Sort States/UTs by total
sorted_df = df.sort_values("Total",ascending=False)

print("\nState/UTs sorted by total:")
print(sorted_df[["State/UT", "Category", "Total"]])

# Top 10 States/UTs
top_10 = df.sort_values("Total",ascending=False).head(10)
print("\nTop 10 States/UTs:")
print(top_10[["State/UT", "Total"]])

# Bottom 10 States/UTs
bottom_10 = df.sort_values("Total",ascending=True).head(10)
print("\nBottom 10 States/UTs:")
print(bottom_10[["State/UT", "Total"]])

# Average for States
states = df[df["Category"] == "State"]
print("\nAverage for States:")
print(states["Total"].mean())

# Average for UTs
uts = df[df["Category"] == "UT"]
print("\nAverage for UTs:")
print(uts["Total"].mean())

# Total for States
print("\nTotal for all States:")
print(states["Total"].sum())

# Total for UTs
print("\nTotal for all UTs:")
print(uts["Total"].sum())