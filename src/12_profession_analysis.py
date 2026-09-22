import pandas as pd

df = pd.read_csv("Data/Cause-wise Distribution_professional_status_2021.csv",encoding="cp1252")

# Remove total rows
df = df[
    (df["State/UT"] != "Total (States)") &
    (df["State/UT"] != "Total (UTs)") &
    (df["State/UT"] != "Total (All India)")
].copy()

# Show State/UT and total
print("\nProfessional data by State/UT:")
print(df[["State/UT", "Total - Total"]])

# Top 10 States/UTs
top_10 = df.sort_values("Total - Total",ascending=False).head(10)
print("\nTop 10 States/UTs:")
print(top_10[["State/UT", "Total - Total"]])

# Total recorded cases
print("\nTotal cases in professional dataset:")
print(df["Total - Total"].sum())