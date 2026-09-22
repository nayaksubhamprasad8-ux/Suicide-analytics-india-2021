import pandas as pd

df = pd.read_csv("Data/master_state_dataset_2021.csv")

male_total = df["Male"].sum()
female_total = df["Female"].sum()
transgender_total = df["Transgender"].sum()

print("\nGender Totals:")
print("Male:", male_total)
print("Female:", female_total)
print("Transgender:", transgender_total)

# Percentage by gender
total = male_total + female_total + transgender_total
male_percentage = (male_total / total) * 100
female_percentage = (female_total / total) * 100
transgender_percentage = (transgender_total / total) * 100

print("\nGender Percentages:")
print("Male:", round(male_percentage, 2), "%")
print("Female:", round(female_percentage, 2), "%")
print("Transgender:", round(transgender_percentage, 2), "%")

# State/UT with highest male count

highest_male = df.loc[df["Male"].idxmax()]
print("\nHighest Male Count:")
print("State/UT:", highest_male["State/UT"])
print("Male:", highest_male["Male"])

# State/UT with highest female count
highest_female = df.loc[df["Female"].idxmax()]
print("\nHighest Female Count:")
print("State/UT:", highest_female["State/UT"])
print("Female:", highest_female["Female"])

# Top 5 States/UTs by male count
top_male = df.sort_values("Male",ascending=False).head(5)
print("\nTop 5 States/UTs by Male Count:")
print(top_male[["State/UT", "Male"]])

# Top 5 States/UTs by female count
top_female = df.sort_values("Female",ascending=False).head(5)
print("\nTop 5 States/UTs by Female Count:")
print(top_female[["State/UT", "Female"]])