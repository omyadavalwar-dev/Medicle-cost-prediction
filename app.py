import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Page Configuration
st.set_page_config(page_title="Medical Insurance Cost Predictor", page_icon="🏥", layout="centered")

st.title("🏥 Medical Insurance Cost Prediction")
st.write("Enter the details below to predict the estimated medical insurance charges.")

# Load Dataset & Train Model
@st.cache_data
def train_model():
    df = pd.read_csv('insurance.csv')
    X = df.drop(columns=["charges", "region"]).copy()
    X["sex"] = X["sex"].map({"female": 1, "male": 0})
    X["smoker"] = X["smoker"].map({"yes": 1, "no": 0})
    y = df["charges"]
    
    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

# User Input Form
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0, step=0.1)

with col2:
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker Status", ["no", "yes"])

# Encode inputs
sex_val = 1 if sex == "female" else 0
smoker_val = 1 if smoker == "yes" else 0

# Predict Button
if st.button("Predict Insurance Cost", type="primary"):
    input_data = np.array([[age, sex_val, bmi, children, smoker_val]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"💰 Estimated Medical Insurance Cost: **${prediction:,.2f}**")