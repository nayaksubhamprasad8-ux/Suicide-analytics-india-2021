import pandas as pd
import plotly.express as plt

df = pd.read_csv("Data/Cause-wise Distribution_mode_2021.csv",encoding="cp1252")

# Sort modes by total
df = df.sort_values("Total",ascending=False)

print("\nModes:")
print(df[["Cause", "Total", "Percentage Share"]])

# Create horizontal bar chart
fig = plt.bar(
    df,
    x="Total",
    y="Cause",
    orientation="h",
    title="Reported Modes - India 2021",
    labels={
        "Total": "Total Recorded Cases",
        "Cause": "Reported Mode"
    }
)
fig.update_layout(yaxis={"categoryorder": "total ascending"})
fig.show()