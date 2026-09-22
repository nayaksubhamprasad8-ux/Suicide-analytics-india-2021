# Suicide Analytics — India 2021

A Python-based data analysis and interactive **Streamlit dashboard** for exploring suicide-related data reported across the States and Union Territories of India for **2021**.

The project focuses on descriptive analysis of the provided dataset, covering geographic distribution, gender, reported causes, reported modes, educational status, and professional status.

> **Disclaimer:** This project is intended for educational and descriptive data-analysis purposes. Recorded counts should not be interpreted as individual-level suicide risk or population suicide rates without appropriate population denominators.

---

## 📊 Project Overview

The project takes multiple raw CSV datasets, cleans and validates the data, performs exploratory analysis, creates visualizations, and presents the results through an interactive Streamlit dashboard.

### Main areas of analysis

- State and Union Territory distribution
- Gender distribution
- Reported causes
- Reported modes
- Educational status
- Professional status
- Descriptive statistics and comparisons

---

## 🚀 Dashboard

The Streamlit dashboard contains the following sections:

### 1. Overview

Provides a high-level summary of the dataset:

- Total recorded cases
- Male, female, and transgender counts
- Number of States and Union Territories
- Gender percentages
- Gender distribution chart
- Top 10 States/UTs
- Key descriptive insights

### 2. State Analysis

Allows users to explore individual States and Union Territories:

- Total recorded cases
- Male cases
- Female cases
- Transgender cases
- Education dataset total
- Professional dataset total
- State/UT comparison

### 3. Gender Analysis

Provides:

- Male, female, and transgender totals
- Gender percentages
- Gender distribution
- Gender comparison charts

### 4. Cause Analysis

Displays the distribution of **reported causes**, including the top reported causes in the dataset.

### 5. Mode Analysis

Displays the distribution of **reported modes** across the dataset.

### 6. Education Analysis

Shows recorded totals by State/UT from the educational-status dataset.

### 7. Professional Analysis

Shows recorded totals by State/UT from the professional-status dataset.

---

## 📁 Dataset

The project uses the following source datasets:

```text
Data/
│
├── Cause-wise Distribution_2021.csv
├── Cause-wise Distribution_economic_status_2021.csv
├── Cause-wise Distribution_educational_status_2021.csv
├── Cause-wise Distribution_mode_2021.csv
├── Cause-wise Distribution_professional_status_2021.csv
└── State-wise Distribution_2021.csv
```

A cleaned master dataset is also generated during the data-processing stage:

```text
Data/
└── master_state_dataset_2021.csv
```

### Dataset descriptions

| Dataset | Description |
|---|---|
| `Cause-wise Distribution_2021.csv` | Distribution of reported causes by age group and gender |
| `Cause-wise Distribution_economic_status_2021.csv` | Distribution across economic/marital-status categories |
| `Cause-wise Distribution_educational_status_2021.csv` | Distribution by educational status across States/UTs |
| `Cause-wise Distribution_mode_2021.csv` | Distribution of reported modes |
| `Cause-wise Distribution_professional_status_2021.csv` | Distribution by professional status across States/UTs |
| `State-wise Distribution_2021.csv` | State/UT-level distribution by reported mode and gender |
| `master_state_dataset_2021.csv` | Cleaned State/UT master dataset created during processing |

---

## 🗂️ Project Structure

```text
Suicide-analytics-india-2021/
│
├── app/
│   └── dashboard.py
│
├── Data/
│   ├── Cause-wise Distribution_2021.csv
│   ├── Cause-wise Distribution_economic_status_2021.csv
│   ├── Cause-wise Distribution_educational_status_2021.csv
│   ├── Cause-wise Distribution_mode_2021.csv
│   ├── Cause-wise Distribution_professional_status_2021.csv
│   ├── State-wise Distribution_2021.csv
│   └── master_state_dataset_2021.csv
│
│
├── src/
│   ├── inspect_data.py
│   ├── 01_explore_data.py
│   ├── 02_clean_state_data.py
│   ├── 03_validate_data.py
│   ├── 04_compare_totals.py
│   ├── 05_create_master_dataset.py
│   ├── 06_basic_analysis.py
│   ├── 07_gender_analysis.py
│   ├── 08_state_analysis.py
│   ├── 09_cause_analysis.py
│   ├── 10_mode_analysis.py
│   ├── 11_education_analysis.py
│   ├── 12_profession_analysis.py
│   ├── 13_gender_visualization.py
│   ├── 14_state_visualization.py
│   ├── 15_cause_visualization.py
│   ├── 16_mode_visualization.py
│   ├── 17_education_visualization.py
│   └── 18_profession_visualization.py
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas** — Data cleaning and analysis
- **Plotly** — Interactive visualizations
- **Streamlit** — Interactive dashboard
- **CSV** — Dataset format
- **Git & GitHub** — Version control and project hosting

---

## 🔎 Data Processing Workflow

The project follows this workflow:

```text
Raw CSV Files
      ↓
Data Inspection
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
Master Dataset Creation
      ↓
Exploratory Data Analysis
      ↓
Visualization
      ↓
Streamlit Dashboard
```

The processing scripts are located in the `src/` directory.

---

## 📈 Analysis Performed

The project performs descriptive analysis including:

- Total recorded cases
- Average recorded cases by State/UT
- Highest and lowest recorded totals
- Male, female, and transgender totals
- Gender percentages
- Top reported causes
- Reported mode distribution
- Educational-status distribution
- Professional-status distribution
- State and Union Territory comparisons

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Move into the project directory

```bash
cd Suicide-analytics-india-2021
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

Start the Streamlit application with:

```bash
streamlit run app/dashboard.py
```

The application will open in your browser.

The default local address is:

```text
http://localhost:8501
```

---

## 🎯 Project Goals

The main goals of this project are to:

1. Practice data cleaning and manipulation using Pandas.
2. Work with a real-world dataset.
3. Perform exploratory data analysis.
4. Validate and organize multiple datasets.
5. Create meaningful data visualizations.
6. Build an interactive dashboard using Streamlit.
7. Present data findings in a clear and accessible format.

---

## 🚀 Future Improvements

Possible future improvements include:

- Adding data from additional years
- Comparing distributions across multiple years
- Expanding educational-status analysis
- Adding economic-status analysis to the dashboard
- Adding more interactive but simple filters
- Adding downloadable reports
- Deploying the dashboard online

---

## 👨‍💻 Author

**Subham Prasad Nayak**

Built as a data analysis and visualization project using **Python, Pandas, Plotly, and Streamlit**.
