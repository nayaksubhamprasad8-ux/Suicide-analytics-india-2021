import pandas as pd
import plotly.express as plt

df = pd.read_csv("Data/Cause-wise Distribution_2021.csv",encoding="cp1252")

# Get top 10 causes
top_10 = df.sort_values("Total - Total",ascending=False).head(10)
print("\nTop 10 Causes:")
print(top_10[["Cause", "Total - Total"]])

# Create horizontal bar chart
fig = plt.bar(
    top_10,
    x="Total - Total",
    y="Cause",
    orientation="h",
    title="Top 10 Reported Causes - India 2021",
    labels={
        "Total - Total": "Total Recorded Cases",
        "Cause": "Reported Cause"
    }
)
fig.update_layout(yaxis={"categoryorder": "total ascending"})
fig.show()