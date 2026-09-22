import pandas as pd
import plotly.express as plt

df = pd.read_csv("Data/Cause-wise Distribution_professional_status_2021.csv",encoding="cp1252")

# Remove total rows
df = df[
    (df["State/UT"] != "Total (States)") &
    (df["State/UT"] != "Total (UTs)") &
    (df["State/UT"] != "Total (All India)")
].copy()

# Get top 10 States/UTs
top_10 = df.sort_values("Total - Total",ascending=False).head(10)
print("\nTop 10 States/UTs - Professional Dataset:")
print(top_10[["State/UT", "Total - Total"]])

# Create horizontal bar chart
fig = plt.bar(
    top_10,
    x="Total - Total",
    y="State/UT",
    orientation="h",
    title="Top 10 States/UTs - Professional Status (2021)",
    labels={
        "Total - Total": "Total Recorded Cases",
        "State/UT": "State/UT"
    }
)
fig.update_layout(yaxis={"categoryorder": "total ascending"})
fig.show()