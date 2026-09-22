import pandas as pd

education = pd.read_csv("Data/Cause-wise Distribution_educational_status_2021.csv", encoding="cp1252")
profession = pd.read_csv("Data/Cause-wise Distribution_professional_status_2021.csv",encoding="cp1252")
state = pd.read_csv("Data/State-wise Distribution_2021.csv",encoding="cp1252")

education = education[
    (education["State/UT"] != "Total (States)") &
    (education["State/UT"] != "Total (UTs)") &
    (education["State/UT"] != "Total (All India)")
].copy()

profession = profession[
    (profession["State/UT"] != "Total (States)") &
    (profession["State/UT"] != "Total (UTs)") &
    (profession["State/UT"] != "Total (All India)")
].copy()

state = state[
    (state["State/UT"] != "Total (States)") &
    (state["State/UT"] != "Total (UTs)") &
    (state["State/UT"] != "Total (All India)")
].copy()

master = state[
    [
        "Category",
        "State/UT",
        "Total - Male",
        "Total - Female",
        "Total - Transgender",
        "Total - Total"
    ]
].copy()

master.columns = [
    "Category",
    "State/UT",
    "Male",
    "Female",
    "Transgender",
    "Total"
]

master["Education_Total"] = education["Total - Total"].values
master["Profession_Total"] = profession["Total - Total"].values

print("\nMaster Dataset:")
print(master)

print("\nShape:")
print(master.shape)

master.to_csv("Data/master_state_dataset_2021.csv",index=False)
print("\nMaster dataset saved!")