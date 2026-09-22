import pandas as pd
import os

DATA_DIR = "Data"

education_path = os.path.join(DATA_DIR,"Cause-wise Distribution_educational_status_2021.csv")
education_df = pd.read_csv(education_path,encoding="cp1252")

print("Original shape:")
print(education_df.shape)
aggregate_rows = ["Total (States)","Total (UTs)","Total (All India)"]
education_clean = education_df[education_df["State/UT"] != "Total (States)"]
education_clean = education_clean[education_clean["State/UT"] != "Total (UTs)"]
education_clean = education_clean[education_clean["State/UT"] != "Total (All India)"].copy()

print("\nCleaned shape:")
print(education_clean.shape)

print("\nCategory counts:")
print(education_clean["Category"].value_counts())

print("\nFirst 5 rows:")
print(education_clean[["Category", "State/UT"]].head())

print("\nLast 5 rows:")
print(education_clean[["Category", "State/UT"]].tail())