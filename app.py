
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("child_nutrition_model.pkl")

st.set_page_config(
    page_title="Child Nutrition Predictor",
    page_icon="🧒",
    layout="centered"
)

st.title("🧒 Child Nutrition Status Predictor")

st.write(
    "Enter the child's basic anthropometric measurements "
    "to predict the nutrition status using a Machine Learning model."
)

st.divider()

age = st.number_input(
    "Age (months)",
    min_value=0.0,
    max_value=60.0,
    value=24.0,
    step=1.0
)

weight = st.number_input(
    "Weight (kg)",
    min_value=0.1,
    max_value=30.0,
    value=8.0,
    step=0.1
)

height = st.number_input(
    "Height (cm)",
    min_value=30.0,
    max_value=150.0,
    value=75.0,
    step=0.1
)

muac = st.number_input(
    "MUAC (cm)",
    min_value=5.0,
    max_value=25.0,
    value=11.0,
    step=0.1
)

st.divider()

if st.button("🔍 Predict Nutrition Status", use_container_width=True):

    input_data = pd.DataFrame({
        "age_months": [age],
        "weight_kg": [weight],
        "height_cm": [height],
        "muac_cm": [muac]
    })

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")

    st.success(
        f"Predicted Nutrition Status: **{prediction.title()}**"
    )

    st.subheader("Prediction Probabilities")

    probability_df = pd.DataFrame({
        "Nutrition Status": model.classes_,
        "Probability": probabilities
    })

    probability_df["Probability"] = (
        probability_df["Probability"] * 100
    ).round(2)

    st.dataframe(
        probability_df,
        hide_index=True,
        use_container_width=True
    )

st.divider()

st.caption(
    "This application is an educational machine learning project "
    "and should not be used as a medical diagnosis."
)
