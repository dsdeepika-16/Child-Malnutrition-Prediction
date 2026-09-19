
import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("child_nutrition_model.pkl")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Child Nutrition Predictor",
    page_icon="🧒",
    layout="wide"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧒 Child Nutrition")

st.sidebar.caption("Design Thinking Project")

page = st.sidebar.radio(
    "Explore the Project",
    [
        "🏠 Home",
        "❤️ Understanding the Problem",
        "🎯 Problem Statement",
        "💡 Possible Solutions",
        "🛠️ Nutrition Predictor",
        "🧪 Test & Give Feedback"
    ]
)


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.title("🧒 Child Nutrition Status Prediction")

    st.subheader(
        "A Design Thinking & Machine Learning Project"
    )

    st.write(
        "This project addresses a real-world social problem related "
        "to child nutrition and develops a simple Machine Learning "
        "prototype for preliminary nutrition-status screening."
    )

    st.divider()

    st.header("🎯 Project Objective")

    st.write(
        "To develop a simple and accessible Machine Learning prototype "
        "that uses basic anthropometric measurements to provide a "
        "preliminary prediction of a child's nutrition status."
    )

    st.divider()

    st.header("💭 Design Thinking Journey")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("### ❤️")
        st.markdown("**Empathize**")
        st.caption("Understand the people and their problems.")

    with col2:
        st.markdown("### 🎯")
        st.markdown("**Define**")
        st.caption("Frame the problem clearly.")

    with col3:
        st.markdown("### 💡")
        st.markdown("**Ideate**")
        st.caption("Explore possible solutions.")

    with col4:
        st.markdown("### 🛠️")
        st.markdown("**Prototype**")
        st.caption("Build the proposed solution.")

    with col5:
        st.markdown("### 🧪")
        st.markdown("**Test**")
        st.caption("Collect feedback and improve.")

    st.divider()

    st.info(
        "⚠️ This is an educational Machine Learning prototype. "
        "It is not a medical diagnostic tool."
    )


# ============================================================
# EMPATHIZE
# ============================================================

elif page == "❤️ Understanding the Problem":

    st.title("❤️ Empathize")

    st.subheader("Understanding the People and Their Needs")

    st.write(
        "The Empathize stage focuses on understanding the people "
        "affected by the problem and the difficulties they may face."
    )

    st.divider()

    st.header("👥 Who is affected?")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 👶 Children")

        st.write(
            "Children may experience poor nutritional status, "
            "which can affect healthy growth and development."
        )

        st.markdown("### 👨‍👩‍👧 Parents & Caregivers")

        st.write(
            "Parents and caregivers may have basic measurements "
            "such as height and weight but may not know how to "
            "interpret them in relation to nutrition status."
        )

    with col2:

        st.markdown("### 🧑‍⚕️ Health & Community Workers")

        st.write(
            "Community or health workers may work with many "
            "children and may benefit from simple digital tools "
            "for preliminary screening."
        )

        st.markdown("### 🌍 Community")

        st.write(
            "Improving awareness and supporting early identification "
            "of possible nutritional concerns can be valuable at "
            "the community level."
        )

    st.divider()

    st.header("🔍 User Need Identified")

    st.success(
        "A simple and understandable tool that can use basic "
        "child measurements to provide a preliminary indication "
        "of nutrition status."
    )

    st.warning(
        "The Empathize stage should be strengthened with real "
        "user interaction or survey evidence as part of the project."
    )


# ============================================================
# DEFINE
# ============================================================

elif page == "🎯 Problem Statement":

    st.title("🎯 Define")

    st.subheader("Clearly Framing the Problem")

    st.write(
        "After understanding the users and their needs, the next "
        "step is to define the specific problem that the project "
        "will address."
    )

    st.divider()

    st.header("📌 Problem Statement")

    st.markdown(
        """
        > **Parents, caregivers and frontline health workers may
        > face difficulty in quickly identifying possible poor
        > nutritional status in children using basic growth
        > measurements. There is a need for a simple and accessible
        > tool that can assist in preliminary nutrition-status screening.**
        """
    )

    st.divider()

    st.header("💭 How Might We...?")

    st.info(
        "**How might we make preliminary child nutrition-status "
        "screening simpler and more accessible using basic "
        "anthropometric measurements?**"
    )

    st.divider()

    st.header("🎯 Design Goal")

    st.write(
        "To develop a simple Machine Learning-based prototype "
        "that accepts basic anthropometric measurements and "
        "provides a preliminary prediction of nutrition status."
    )


# ============================================================
# IDEATE
# ============================================================

elif page == "💡 Possible Solutions":

    st.title("💡 Ideate")

    st.subheader("Exploring Multiple Possible Solutions")

    st.write(
        "Before selecting the final solution, multiple ideas "
        "were considered to address the identified problem."
    )

    st.divider()

    solutions = [
        (
            "🥗 Nutrition Awareness Tool",
            "Provide simple educational information about child "
            "nutrition and nutritional awareness."
        ),
        (
            "📊 Child Growth Tracking System",
            "Allow caregivers or health workers to record and "
            "monitor children's growth measurements."
        ),
        (
            "📋 Manual Nutrition Assessment Guide",
            "Provide an easy-to-understand guide for interpreting "
            "basic anthropometric measurements."
        ),
        (
            "🤖 ML Nutrition Prediction Tool",
            "Use child measurements to provide a preliminary "
            "prediction of nutrition status."
        ),
        (
            "🧑‍⚕️ Community Screening Support Tool",
            "Provide a digital tool that could support preliminary "
            "screening by community or health workers."
        )
    ]

    for title, description in solutions:

        with st.expander(title):

            st.write(description)

    st.divider()

    st.header("💡 Selected Solution")

    st.success(
        "🤖 Machine Learning-based Child Nutrition Status "
        "Prediction Prototype"
    )

    st.write(
        "The selected idea combines basic anthropometric "
        "measurements with Machine Learning to create a simple "
        "digital prototype."
    )


# ============================================================
# PROTOTYPE / ML PREDICTOR
# ============================================================

elif page == "🛠️ Nutrition Predictor":

    st.title("🛠️ Prototype")

    st.subheader("Child Nutrition Status Predictor")

    st.write(
        "Enter the child's basic anthropometric measurements "
        "to generate a preliminary nutrition-status prediction."
    )

    st.divider()

    st.header("🤖 Machine Learning Model")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Algorithm**")
        st.write("Decision Tree Classifier")

        st.markdown("**Input Features**")
        st.write(
            "• Age (months)\n"
            "• Weight (kg)\n"
            "• Height (cm)\n"
            "• MUAC (cm)"
        )

    with col2:

        st.markdown("**Output Classes**")
        st.write(
            "• Normal\n"
            "• Moderate\n"
            "• Severe"
        )

        st.markdown("**Class Weighting**")
        st.write("Balanced")

    st.divider()

    st.header("📋 Enter Child Measurements")

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

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

    if st.button(
        "🔍 Predict Nutrition Status",
        use_container_width=True
    ):

        input_data = pd.DataFrame({
            "age_months": [age],
            "weight_kg": [weight],
            "height_cm": [height],
            "muac_cm": [muac]
        })

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        st.divider()

        st.header("📊 Prediction Result")

        if prediction.lower() == "normal":

            st.success(
                f"Predicted Nutrition Status: **{prediction.title()}**"
            )

        elif prediction.lower() == "moderate":

            st.warning(
                f"Predicted Nutrition Status: **{prediction.title()}**"
            )

        else:

            st.error(
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
        "⚠️ Educational prototype only. Predictions should not "
        "be considered a medical diagnosis."
    )


# ============================================================
# TEST & FEEDBACK
# ============================================================

elif page == "🧪 Test & Give Feedback":

    st.title("🧪 Test & Give Feedback")

    st.subheader("Usability Testing")

    st.write(
        "Your feedback will help us understand whether the "
        "prototype is easy to use and how it can be improved."
    )

    st.divider()

    st.header("📝 Feedback Form")

    with st.form("feedback_form"):

        rating = st.slider(
            "⭐ How would you rate your overall experience?",
            min_value=1,
            max_value=5,
            value=5
        )

        easy_to_use = st.radio(
            "👍 Was the application easy to use?",
            ["Yes", "No"]
        )

        clear_inputs = st.radio(
            "🔍 Were the input fields clear and understandable?",
            ["Yes", "No"]
        )

        clear_result = st.radio(
            "📊 Was the prediction result easy to understand?",
            ["Yes", "No"]
        )

        useful = st.radio(
            "💡 Would you find this type of tool useful?",
            ["Yes", "No", "Maybe"]
        )

        useful_feature = st.selectbox(
            "Which part of the application did you find most useful?",
            [
                "Nutrition information",
                "Input section",
                "Prediction result",
                "Prediction probabilities",
                "Overall design"
            ]
        )

        what_worked = st.text_area(
            "✅ What did you like or find useful?"
        )

        improvement = st.text_area(
            "🔧 What could be improved?"
        )

        submitted = st.form_submit_button(
            "📤 Submit Feedback",
            use_container_width=True
        )

    if submitted:

        feedback = pd.DataFrame([{
            "Date_Time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "Rating": rating,
            "Easy_to_Use": easy_to_use,
            "Clear_Inputs": clear_inputs,
            "Clear_Result": clear_result,
            "Useful": useful,
            "Most_Useful_Feature": useful_feature,
            "What_Worked": what_worked,
            "Improvement": improvement
        }])

        file_name = "user_feedback.csv"

        if os.path.exists(file_name):

            feedback.to_csv(
                file_name,
                mode="a",
                header=False,
                index=False
            )

        else:

            feedback.to_csv(
                file_name,
                index=False
            )

        st.success(
            "✅ Thank you! Your feedback has been recorded."
        )

        st.balloons()

    st.divider()

    st.header("🔄 From Feedback to Improvement")

    st.write(
        "The collected feedback can be reviewed to identify "
        "usability problems and make improvements to the prototype."
    )

    st.markdown(
        """
        **Prototype → Test → Feedback → Improvement → Updated Prototype**
        """
    )

    st.info(
        "The feedback collected here can be analyzed and presented "
        "in the Test stage of the Design Thinking presentation."
    )

    st.caption(
        "Feedback is collected for academic project evaluation "
        "and prototype improvement."
    )
