Insurance Risk Analytics & Predictive Modeling
Project Overview

This project focuses on end-to-end insurance risk analytics using historical automobile insurance data from AlphaCare Insurance Solutions (ACIS) in South Africa. The objective is to analyze customer, vehicle, policy, and claims data to uncover low-risk customer segments and support data-driven insurance pricing strategies.

The project includes:

Exploratory Data Analysis (EDA)
Risk and profitability analysis
Data Version Control (DVC)
Statistical hypothesis testing
Predictive modeling
Risk-based pricing insights

Business Objective

AlphaCare Insurance Solutions (ACIS) aims to optimize marketing strategy and improve premium pricing decisions using historical insurance claim data.

The key goals are:

Identify low-risk customer segments
Analyze claim behavior across provinces, vehicle types, and demographics
Understand profitability using Loss Ratio and Margin metrics
Build reproducible analytics pipelines
Support future predictive risk modeling

Dataset Description

The dataset contains approximately 18 months of historical car insurance data from February 2014 to August 2015.

Main Data Categories
Category	Examples
Policy	   PolicyID, UnderwrittenCoverID
Client	   Gender, MaritalStatus, Citizenship
Vehicle	   Make, Model, VehicleType
Location   Province, PostalCode
Plan	   SumInsured, CoverType
Financial  TotalPremium, TotalClaims

Key Metrics
Loss Ratio
Loss Ratio = TotalClaims / TotalPremium

Measures insurance portfolio risk and profitability.

Margin
Margin = TotalPremium - TotalClaims

Measures profit contribution per policy.

Exploratory Data Analysis (EDA)

The EDA phase includes:

Data summarization
Missing value analysis
Outlier detection
Geographic risk analysis
Vehicle claim analysis
Financial variable distributions
Temporal trend analysis
Correlation analysis
Main Insights Explored
Portfolio Loss Ratio
Claims by Province
Claims by Gender
VehicleType risk comparison
Monthly claims trends
Premium vs Claims relationships

Technologies Used

Programming Language
Python
Data Analysis
pandas
numpy
Visualization
matplotlib
seaborn
plotly
Machine Learning
scikit-learn
XGBoost
Data Version Control
DVC
Development Tools
Git
GitHub
GitHub Actions
Jupyter Notebook


CI/CD Pipeline

GitHub Actions is configured to automatically:

Run tests
Validate code quality
Check project consistency

on every push and pull request.

Future Work
Statistical hypothesis testing
Claim severity prediction
Claim probability modeling
Risk-based premium optimization
Model explainability using SHAP


Author

Hana Lemma