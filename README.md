# FINANCE – Debit Card Fraud Detection

## Project Overview

This project aims to identify potentially fraudulent debit card transactions using Machine Learning techniques.

The objective is to analyse transaction patterns, identify suspicious behaviour, and develop a classification model that can distinguish between genuine and fraudulent transactions.

## Dataset

**Source:** [Kaggle – Transactions Fraud Datasets](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets)

The project uses the debit card transactions extracted from the original dataset.

- Total labelled transactions: 5,548,196
- Genuine transactions: 5,540,732
- Fraudulent transactions: 7,464
- Fraud percentage: 0.1345%

The dataset is synthetic and is used for educational and machine learning experimentation.

## Initial Exploratory Data Analysis

Initial analysis identified interesting patterns:

- Online transactions have a higher observed fraud rate than chip and swipe transactions.
- Higher transaction amounts show varying fraud rates.
- Merchant categories have different observed fraud rates.
- Transactions with recorded errors show a higher fraud rate.
- Fraud rates vary across transaction hours.

## Planned Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit

## Project Roadmap

1. Dataset inspection and validation
2. Exploratory Data Analysis
3. Feature engineering
4. Data preprocessing
5. Baseline model development
6. Machine Learning model training
7. Model evaluation
8. Streamlit demonstration

## Expected Outcome

A simple fraud detection application that accepts transaction details and predicts whether a transaction is potentially fraudulent.
