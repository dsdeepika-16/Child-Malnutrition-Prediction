# 🧒 Child Nutrition Status Prediction Using Machine Learning

## 📌 Project Overview

This project uses Machine Learning to predict the nutrition status of a child based on basic anthropometric measurements.

The project focuses on three nutrition status categories:

- Normal
- Moderate
- Severe

A Decision Tree Classifier is used to perform the prediction.

## 🎯 Objective

The objective of this project is to demonstrate how Machine Learning can be applied to a social and public-health-related problem such as child nutrition assessment.

## 📊 Dataset

The dataset contains 5,000 child-level observations with the following variables:

- Age (months)
- Weight (kg)
- Height (cm)
- MUAC (cm)
- Nutrition Status

The target variable is `nutrition_status`.

## 🤖 Machine Learning Model

A Decision Tree Classifier was developed and evaluated.

The final model uses:

- Criterion: Gini
- Maximum Depth: 10
- Class Weight: Balanced
- Random State: 42

Class balancing was used to improve the model's ability to identify less frequent nutrition-status categories.

## 📈 Model Evaluation

The final model achieved approximately:

- Accuracy: 91.6%
- Balanced Accuracy: 86.1%
- Macro F1-score: 83.0%

The model was also evaluated using 5-fold stratified cross-validation.

## 🔑 Important Features

The final Decision Tree identified the following feature importance values:

| Feature | Importance |
|---|---:|
| MUAC | 67.30% |
| Age (months) | 14.90% |
| Weight (kg) | 12.69% |
| Height (cm) | 5.11% |

## 🌐 Streamlit Application

The trained model is deployed as an interactive Streamlit application.

Users can enter:

- Age
- Weight
- Height
- MUAC

and receive a predicted nutrition-status category along with model probabilities.

## 📁 Project Structure

```text
Child-Malnutrition-Prediction/
│
├── app.py
├── requirements.txt
├── child_nutrition_model.pkl
├── malnutrition_data.csv
├── Child_Malnutrition.ipynb
└── README.md
