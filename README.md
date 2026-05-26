# Insurance Risk Analytics & Predictive Modeling

## Project Overview

This project focuses on end-to-end insurance risk analytics using historical automobile insurance data from AlphaCare Insurance Solutions (ACIS) in South Africa. The goal is to analyze customer, vehicle, policy, and claims data to identify low-risk customer segments and support data-driven insurance pricing strategies.

The project includes:
- Exploratory Data Analysis (EDA)
- Risk and profitability analysis
- Statistical hypothesis testing
- Predictive modeling
- Data Version Control (DVC)
- Risk-based pricing insights

---

# Business Objective

The main objectives are to:
- Identify low-risk customer segments
- Analyze claim behavior across provinces, vehicle types, and demographics
- Measure profitability using Loss Ratio and Margin metrics
- Build reproducible analytics pipelines
- Support predictive risk modeling

---

# Dataset Description

The dataset contains approximately 18 months of historical automobile insurance data from February 2014 to August 2015.

## Main Features

| Category | Examples |
|---|---|
| Policy | PolicyID, UnderwrittenCoverID |
| Client | Gender, MaritalStatus |
| Vehicle | Make, Model, VehicleType |
| Location | Province, PostalCode |
| Financial | TotalPremium, TotalClaims |

---

# Key Metrics

## Loss Ratio

Loss Ratio = TotalClaims / TotalPremium

Measures insurance portfolio risk and profitability.

## Margin

Margin = TotalPremium - TotalClaims

Measures profit contribution per policy.

---

# Project Structure

```bash
insurance-risk-analytics/
│
├── data/
├── notebooks/
├── reports/
├── src/
├── tests/
├── .github/workflows/
├── requirements.txt
├── dvc.yaml
└── README.md
```

---

# Exploratory Data Analysis (EDA)

The EDA phase includes:
- Missing value analysis
- Outlier detection
- Geographic risk analysis
- Vehicle claim analysis
- Financial trend analysis
- Correlation analysis

## Key Insights Explored
- Portfolio Loss Ratio
- Claims by Province
- Claims by Gender
- VehicleType risk comparison
- Monthly claims trends
- Premium vs Claims relationships

---

# Predictive Modeling

The project supports:
- Claim severity prediction
- Claim probability prediction
- Customer risk scoring
- Risk-based pricing

## Algorithms Used
- Linear Regression
- Logistic Regression
- Random Forest
- XGBoost

---

# Technologies Used

- Python
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- scikit-learn
- XGBoost
- DVC
- Git & GitHub
- GitHub Actions
- Jupyter Notebook

---

# CI/CD Pipeline

GitHub Actions is configured to:
- Run tests
- Validate code quality
- Check project consistency

on every push and pull request.

---

# Data Version Control (DVC)

## Initialize DVC

```bash
dvc init
```

## Pull Dataset

```bash
dvc pull
```

## Add Dataset Version

```bash
dvc add data/insurance_data.csv
```

## Push Dataset

```bash
dvc push
```

---

# Installation

## Clone Repository

```bash
git clone <your-repository-url>
cd insurance-risk-analytics
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Linux/macOS
```bash
source venv/bin/activate
```

### Windows
```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

## Open Jupyter Notebook

```bash
jupyter notebook
```

## Run Tests

```bash
pytest
```

---

# Future Work

- Advanced hypothesis testing
- Improved predictive modeling
- Risk-based premium optimization
- Model explainability using SHAP
- Interactive dashboards

---

# Author

Hana Lemma