import pandas as pd
import os


DATA_DIR = "Data"
education_file = os.path.join(DATA_DIR,"Cause-wise Distribution_educational_status_2021.csv")
profession_file = os.path.join(DATA_DIR,"Cause-wise Distribution_professional_status_2021.csv")
state_file = os.path.join(DATA_DIR,"State-wise Distribution_2021.csv")

education = pd.read_csv(education_file,encoding="cp1252")
profession = pd.read_csv(profession_file,encoding="cp1252")
state = pd.read_csv(state_file,encoding="cp1252")

education = education[education["State/UT"] != "Total (States)"]
education = education[education["State/UT"] != "Total (UTs)"]
education = education[education["State/UT"] != "Total (All India)"].copy()

profession = profession[profession["State/UT"] != "Total (States)"]
profession = profession[profession["State/UT"] != "Total (UTs)"]
profession = profession[profession["State/UT"] != "Total (All India)"].copy()

state = state[state["State/UT"] != "Total (States)"]
state = state[state["State/UT"] != "Total (UTs)"]
state = state[state["State/UT"] != "Total (All India)"].copy()

education_totals = education[["State/UT", "Total - Total"]].rename(columns={"Total - Total": "Education_Total"})
profession_totals = profession[["State/UT", "Total - Total"]].rename(columns={"Total - Total": "Profession_Total"})
state_totals = state[["State/UT", "Total - Total"]].rename(columns={"Total - Total": "State_Total"})

comparison = education_totals.merge(profession_totals,on="State/UT",how="outer")
comparison = comparison.merge(state_totals,on="State/UT",how="outer")

comparison["All_Match"] = ((comparison["Education_Total"] == comparison["Profession_Total"])&
(comparison["Education_Total"] == comparison["State_Total"])
)

print("\n" + "=" * 70)
print("TOTAL COMPARISON")
print("=" * 70)

print("\nComparison:")
print(comparison.to_string(index=False))

print("\nNumber of states/UTs:")
print(len(comparison))

print("\nNumber of matches:")
print(comparison["All_Match"].sum())

print("\nNumber of mismatches:")
print((~comparison["All_Match"]).sum())


mismatches = comparison[comparison["All_Match"] == False]
if len(mismatches) == 0:
    print("\nAll State/UT totals match successfully.")
else:
    print("\nMismatched State/UTs:")
    print(mismatches.to_string(index=False))