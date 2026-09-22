import pandas as pd
import plotly.express as plt

df = pd.read_csv("Data/master_state_dataset_2021.csv")

# Get top 10 States/UTs
top_10 = df.sort_values("Total",ascending=False).head(10)
print("\nTop 10 States/UTs:")
print(top_10[["State/UT", "Total"]])

#Bar chart
fig = plt.bar(
    top_10,
    x="Total",
    y="State/UT",
    orientation="h", #Here "h" for horizontal bar chart
    title="Top 10 States/UTs by Recorded Total - 2021",
    labels={
        "Total": "Total Recorded Cases",
        "State/UT": "State/UT"
    }
)
# Put highest value at the top
fig.update_layout(yaxis={"categoryorder": "total ascending"})
fig.show()
