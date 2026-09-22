import pandas as pd

df = pd.read_csv("Data/master_state_dataset_2021.csv",encoding="cp1252")
print("\nDataset Shape:")
print(df.shape)

print("\nTotal number of suicides:")
print(df["Total"].sum())

print("\nAverage suicides per State/UT:")
print(df["Total"].mean())

print("\nMinimum suicides:")
print(df["Total"].min())

print("\nMaximum suicides:")
print(df["Total"].max())


highest = df.loc[df["Total"].idxmax()]
print("\nState/UT with highest number:")
print(highest["State/UT"])
print("Total:", highest["Total"])


lowest = df.loc[df["Total"].idxmin()]
print("\nState/UT with lowest number:")
print(lowest["State/UT"])
print("Total:", lowest["Total"])
print("\nGender totals:")

print("Male:", df["Male"].sum())
print("Female:", df["Female"].sum())
print("Transgender:", df["Transgender"].sum())

top_5 = df.sort_values("Total",ascending=False).head(5)
print("\nTop 5 State/UTs:")
print(top_5[["State/UT", "Total"]])