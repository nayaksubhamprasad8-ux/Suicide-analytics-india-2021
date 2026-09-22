import streamlit as st
import pandas as pd
import plotly.express as plt


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Suicide Analytics India 2021",
    page_icon="📊",
    layout="wide"
)

# LOAD DATA
master_df = pd.read_csv("Data/master_state_dataset_2021.csv")
cause_df = pd.read_csv("Data/Cause-wise Distribution_2021.csv",encoding="cp1252")
mode_df = pd.read_csv("Data/Cause-wise Distribution_mode_2021.csv",encoding="cp1252")
education_df = pd.read_csv("Data/Cause-wise Distribution_educational_status_2021.csv",encoding="cp1252")
profession_df = pd.read_csv("Data/Cause-wise Distribution_professional_status_2021.csv",encoding="cp1252")

# REMOVE AGGREGATE ROWS
education_df = education_df[
    (education_df["State/UT"] != "Total (States)") &
    (education_df["State/UT"] != "Total (UTs)") &
    (education_df["State/UT"] != "Total (All India)")
].copy()
profession_df = profession_df[
    (profession_df["State/UT"] != "Total (States)") &
    (profession_df["State/UT"] != "Total (UTs)") &
    (profession_df["State/UT"] != "Total (All India)")
].copy()

# OVERVIEW VALUES
total_cases = master_df["Total"].sum()
male_total = master_df["Male"].sum()
female_total = master_df["Female"].sum()
transgender_total = master_df["Transgender"].sum()
number_of_states = len(master_df[master_df["Category"] == "State"])
number_of_uts = len(master_df[master_df["Category"] == "UT"])

# GENDER PERCENTAGES
gender_total = (male_total +female_total +transgender_total)
male_percentage = (male_total / gender_total) * 100
female_percentage = (female_total / gender_total) * 100
transgender_percentage = (transgender_total / gender_total) * 100

# AUTOMATIC INSIGHTS
highest_state = master_df.loc[master_df["Total"].idxmax()]
lowest_state = master_df.loc[master_df["Total"].idxmin()]
highest_male_state = master_df.loc[master_df["Male"].idxmax()]
highest_female_state = master_df.loc[master_df["Female"].idxmax()]
highest_cause = cause_df.loc[cause_df["Total - Total"].idxmax()]
highest_mode = mode_df.loc[mode_df["Total"].idxmax()]

# SIDEBAR
st.sidebar.title("📊 Dashboard")
st.sidebar.markdown("### Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "State Analysis",
        "Gender Analysis",
        "Cause Analysis",
        "Mode Analysis",
        "Education Analysis",
        "Professional Analysis"
    ]
)

# OVERVIEW
if page == "Overview":
    st.title("Suicide Analytics — India 2021")
    st.write(
        "An interactive descriptive analysis of suicide-related "
        "data reported across States and Union Territories of India."
    )
    st.divider()

    
    # KPI CARDS
    st.header("Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Total Recorded Cases",
            f"{total_cases:,}"
        )
    with col2:
        st.metric(
            "Male",
            f"{male_total:,}"
        )
    with col3:
        st.metric(
            "Female",
            f"{female_total:,}"
        )
    with col4:
        st.metric(
            "States / UTs",
            f"{number_of_states + number_of_uts}"
        )
    st.write(
        f"States: {number_of_states} | "
        f"Union Territories: {number_of_uts} | "
        f"Transgender: {transgender_total:,}"
    )
    st.divider()

    # GENDER SUMMARY
    st.header("Gender Distribution")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Male",
            f"{male_total:,}",
            f"{male_percentage:.2f}%"
        )
    with col2:
        st.metric(
            "Female",
            f"{female_total:,}",
            f"{female_percentage:.2f}%"
        )
    with col3:
        st.metric(
            "Transgender",
            f"{transgender_total:,}",
            f"{transgender_percentage:.2f}%"
        )
    gender_data = pd.DataFrame({
        "Gender": [
            "Male",
            "Female",
            "Transgender"
        ],
        "Total": [
            male_total,
            female_total,
            transgender_total
        ]
    })
    fig = plt.pie(
        gender_data,
        names="Gender",
        values="Total",
        title="Gender Distribution"
    )
    st.plotly_chart(
        fig,
        width="stretch"
    )
    st.divider()

    # TOP 10 STATES
    st.header("Top 10 States / UTs")
    top_10 = master_df.sort_values("Total",ascending=False).head(10)
    fig = plt.bar(
        top_10,
        x="Total",
        y="State/UT",
        orientation="h",
        title="Top 10 States / UTs",
        labels={
            "Total": "Total Recorded Cases",
            "State/UT": "State / UT"
        }
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(
        fig,
        width="stretch"
    )
    st.divider()

    # AUTOMATIC INSIGHTS
    st.header("Key Descriptive Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.info(
            f"**Highest recorded total:** "
            f"{highest_state['State/UT']} "
            f"({int(highest_state['Total']):,})"
        )
        st.info(
            f"**Lowest recorded total:** "
            f"{lowest_state['State/UT']} "
            f"({int(lowest_state['Total']):,})"
        )
        st.info(
            f"**Highest male count:** "
            f"{highest_male_state['State/UT']} "
            f"({int(highest_male_state['Male']):,})"
        )
    with col2:
        st.info(
            f"**Highest female count:** "
            f"{highest_female_state['State/UT']} "
            f"({int(highest_female_state['Female']):,})"
        )
        st.info(
            f"**Largest reported cause:** "
            f"{highest_cause['Cause']} "
            f"({int(highest_cause['Total - Total']):,})"
        )
        st.info(
            f"**Largest reported mode:** "
            f"{highest_mode['Cause']} "
            f"({int(highest_mode['Total']):,})"
        )

# STATE ANALYSIS
elif page == "State Analysis":
    st.title("State / UT Analysis")
    st.write(
        "Explore recorded totals across States and Union Territories."
    )
    region = st.selectbox(
        "Select Region",
        [
            "All",
            "States",
            "Union Territories"
        ]
    )
    if region == "States":

        state_data = master_df[
            master_df["Category"] == "State"
        ]
    elif region == "Union Territories":

        state_data = master_df[
            master_df["Category"] == "UT"
        ]
    else:

        state_data = master_df.copy()
    
    # STATE DETAIL
    st.subheader("State / UT Details")
    selected_state = st.selectbox(
        "Select a State / UT",
        sorted(
            state_data["State/UT"].tolist()
        )
    )
    selected_data = state_data[
        state_data["State/UT"] == selected_state
    ].iloc[0]
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Total",
            f"{int(selected_data['Total']):,}"
        )
    with col2:
        st.metric(
            "Male",
            f"{int(selected_data['Male']):,}"
        )
    with col3:
        st.metric(
            "Female",
            f"{int(selected_data['Female']):,}"
        )
    with col4:
        st.metric(
            "Transgender",
            f"{int(selected_data['Transgender']):,}"
        )
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Education Dataset Total",
            f"{int(selected_data['Education_Total']):,}"
        )
    with col2:
        st.metric(
            "Professional Dataset Total",
            f"{int(selected_data['Profession_Total']):,}"
        )
    st.divider()
   
    # STATE CHART
    state_data = state_data.sort_values("Total",ascending=False)
    fig = plt.bar(
        state_data,
        x="Total",
        y="State/UT",
        orientation="h",
        title="Recorded Cases by State / UT",
        labels={
            "Total": "Total Recorded Cases",
            "State/UT": "State / UT"
        }
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"},height=900)
    st.plotly_chart(fig,width="stretch")
    st.subheader("State / UT Data")
    st.dataframe(
        state_data[
            [
                "Category",
                "State/UT",
                "Male",
                "Female",
                "Transgender",
                "Total"
            ]
        ],
        width="stretch"
    )

# GENDER ANALYSIS
elif page == "Gender Analysis":
    st.title("Gender Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Male",
            f"{male_total:,}",
            f"{male_percentage:.2f}%"
        )
    with col2:
        st.metric(
            "Female",
            f"{female_total:,}",
            f"{female_percentage:.2f}%"
        )
    with col3:
        st.metric(
            "Transgender",
            f"{transgender_total:,}",
            f"{transgender_percentage:.2f}%"
        )
    gender_data = pd.DataFrame({
        "Gender": [
            "Male",
            "Female",
            "Transgender"
        ],
        "Total": [
            male_total,
            female_total,
            transgender_total
        ]
    })
    fig = plt.pie(gender_data,names="Gender",values="Total",title="Gender Distribution")
    st.plotly_chart(fig,width="stretch")
    fig = plt.bar(
        gender_data,
        x="Gender",
        y="Total",
        title="Total Recorded Cases by Gender",
        labels={
            "Gender": "Gender",
            "Total": "Total Recorded Cases"
        }
    )
    st.plotly_chart(
        fig,
        width="stretch"
    )
    st.subheader("Gender Data")

    st.dataframe(
        gender_data,
        width="stretch"
    )

# CAUSE ANALYSIS
elif page == "Cause Analysis":
    st.title("Reported Cause Analysis")
    st.write("Distribution of reported causes in the 2021 dataset.")
    top_causes = cause_df.sort_values("Total - Total",ascending=False).head(10)
    fig = plt.bar(
        top_causes,
        x="Total - Total",
        y="Cause",
        orientation="h",
        title="Top 10 Reported Causes",
        labels={
            "Total - Total": "Total Recorded Cases",
            "Cause": "Reported Cause"
        }
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"},height=650)
    st.plotly_chart(fig,width="stretch")
    st.subheader("Cause Data")
    st.dataframe(
        top_causes[
            [
                "Cause",
                "Total - Male",
                "Total - Female",
                "Total - Transgender",
                "Total - Total"
            ]
        ],
        width="stretch"
    )

# MODE ANALYSIS
elif page == "Mode Analysis":
    st.title("Reported Mode Analysis")
    st.write("Distribution of reported modes in the 2021 dataset.")
    mode_data = mode_df.sort_values("Total",ascending=False)
    fig = plt.bar(
        mode_data,
        x="Total",
        y="Cause",
        orientation="h",
        title="Reported Modes",
        labels={
            "Total": "Total Recorded Cases",
            "Cause": "Reported Mode"
        }
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"},height=700)
    st.plotly_chart(fig,width="stretch")
    st.subheader("Mode Data")
    st.dataframe(
        mode_data[
            [
                "Cause",
                "Male",
                "Female",
                "Transgender",
                "Total",
                "Percentage Share"
            ]
        ],
        width="stretch"
    )

# EDUCATION ANALYSIS
elif page == "Education Analysis":
    st.title("Education Status Analysis")
    st.write("Recorded totals by State / UT from the education dataset.")
    top_education = education_df.sort_values("Total - Total",ascending=False).head(10)
    fig = plt.bar(
        top_education,
        x="Total - Total",
        y="State/UT",
        orientation="h",
        title="Top 10 States / UTs — Education Dataset",
        labels={
            "Total - Total": "Total Recorded Cases",
            "State/UT": "State / UT"
        }
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig,width="stretch")
    st.subheader("Education Data")
    st.dataframe(
        top_education[
            [
                "State/UT",
                "Total - Male",
                "Total - Female",
                "Total - Transgender",
                "Total - Total"
            ]
        ],
        width="stretch"
    )

# PROFESSIONAL ANALYSIS
elif page == "Professional Analysis":
    st.title("Professional Status Analysis")
    st.write(
        "Recorded totals by State / UT from the professional "
        "status dataset."
    )
    top_profession = profession_df.sort_values(
        "Total - Total",
        ascending=False
    ).head(10)
    fig = plt.bar(
        top_profession,
        x="Total - Total",
        y="State/UT",
        orientation="h",
        title="Top 10 States / UTs — Professional Dataset",
        labels={
            "Total - Total": "Total Recorded Cases",
            "State/UT": "State / UT"
        }
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig,width="stretch")
    st.subheader("Professional Status Data")
    st.dataframe(
        top_profession[
            [
                "State/UT",
                "Total - Male",
                "Total - Female",
                "Total - Transgender",
                "Total - Total"
            ]
        ],
        width="stretch"
    )

# FOOTER
st.divider()
st.caption(
    "Suicide Analytics — India 2021 | "
    "Descriptive analysis of the provided dataset"
)