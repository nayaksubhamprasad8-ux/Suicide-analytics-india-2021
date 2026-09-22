import pandas as pd
import os

DATA_DIR = "Data"

path = os.path.join(DATA_DIR,"Cause-wise Distribution_educational_status_2021.csv")
df = pd.read_csv(path, encoding="cp1252")
df = df[(df["State/UT"] != "Total (States)") &(df["State/UT"] != "Total (UTs)") &(df["State/UT"] != "Total (All India)")].copy()
df["Calculated Total"] = (df["Total - Male"]+ df["Total - Female"]+ df["Total - Transgender"])
df["Matches"] = (df["Calculated Total"] == df["Total - Total"])
print("Total rows:", len(df))
print("\nRows where gender total does NOT match:")
print(df.loc[df["Matches"], [
    "State/UT",
    "Total - Male",
    "Total - Female",
    "Total - Transgender",
    "Total - Total",
    "Calculated Total"
]])

print("\nNumber of mismatches:")
print((~df["Matches"]).sum())