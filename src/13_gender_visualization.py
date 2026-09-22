import pandas as pd
import plotly.express as plt

df = pd.read_csv("Data/master_state_dataset_2021.csv")

male = df["Male"].sum()
female = df["Female"].sum()
transgender = df["Transgender"].sum()

gender_data = pd.DataFrame({
    "Gender": ["Male", "Female", "Transgender"],
    "Total": [male, female, transgender]
})

print("\nGender Data:")
print(gender_data)

# Create pie chart
fig = plt.pie(
    gender_data,
    names="Gender",
    values="Total",
    title="Gender Distribution - India 2021"
)
fig.show()