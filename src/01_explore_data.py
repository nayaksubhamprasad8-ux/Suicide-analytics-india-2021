import pandas as pd
import os

DATA_DIR = "Data"

files = {
    "education": "Cause-wise Distribution_educational_status_2021.csv",
    "profession": "Cause-wise Distribution_professional_status_2021.csv",
    "state": "State-wise Distribution_2021.csv"
}
for name, filename in files.items():
    print("\n" + "=" * 70)
    print(name.upper())

    path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(path, encoding='cp1252')  
    print("\nCategory values:")
    print(df['Category'].value_counts())

    print("\nState/UT values:")
    print(df['State/UT'].tolist())

    print("\nNumber of unique values in State/UT:")
    print(df['State/UT'].nunique())