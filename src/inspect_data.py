import pandas as pd
import os

data_dir = "Data"
files = os.listdir(data_dir)

for file in files:
    if file.endswith(".csv"):
        path = os.path.join(data_dir, file)
        df = pd.read_csv(path, encoding='cp1252')  # Use 'cp1252' encoding to handle special characters

        print("\n" + "=" * 70)
        print(file)
        print("=" * 70)

        print("Shape:", df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
        print("\nData Types:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\nFirst 5 Rows:")
        print(df.head())