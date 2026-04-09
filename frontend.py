import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Insurance Predictor", page_icon="💡", layout="centered")

API_URL = "http://localhost:8000/predict"

# Title
st.title("💡 Insurance Premium Predictor")
st.markdown("Enter your details to predict insurance premium category.")

# Input layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
    income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=8.0)
    smoker = st.selectbox("Smoking Habit", ["No", "Yes"])

with col2:
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    city = st.text_input("City", value="Mumbai")
    occupation = st.selectbox("Occupation", [
        'student', 'private_job', 'government_job',
        'business_owner', 'freelancer', 'retired', 'unemployed'
    ])

st.markdown("---")

# Predict Button
if st.button("🚀 Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker == "Yes",
        "city": city,
        "occupation": occupation
    }

    with st.spinner("Analyzing your data..."):
        try:
            response = requests.post(API_URL, json=input_data)

            if response.status_code == 200:
                result = response.json()

                # Extract nested response safely
                response_data = result.get("response", {})

                prediction = response_data.get("predicted_category", "Not Found")
                confidence = response_data.get("confidence", None)
                probabilities = response_data.get("class_probabilities", {})

                # Display results
                st.success(f"Predicted Category: **{prediction}**")

                if confidence is not None:
                    st.info(f"Confidence: {confidence * 100:.2f}%")

                if probabilities:
                    st.write("Class Probabilities:")
                    st.json(probabilities)

            else:
                st.error(f"API Error: {response.status_code}")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to backend. Ensure FastAPI is running on port 8000")

# Footer
st.markdown("---")
st.caption("Built with Streamlit & FastAPI")
