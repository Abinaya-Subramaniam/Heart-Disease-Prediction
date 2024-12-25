import streamlit as st
import joblib
import numpy as np

model = joblib.load("Model.pkl")

st.title("Heart Disease Prediction App ❤️‍🩹")

st.sidebar.header("Input Features")
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.sidebar.selectbox("Sex (1=Male, 0=Female)", [1, 0])
cp = st.sidebar.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.sidebar.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
chol = st.sidebar.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", [1, 0])
restecg = st.sidebar.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.sidebar.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
exang = st.sidebar.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [1, 0])
oldpeak = st.sidebar.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment (0-2)", [0, 1, 2])
ca = st.sidebar.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
thal = st.sidebar.selectbox("Thalium Stress Result (1,3,6,7)", [1, 3, 6, 7])

input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

if st.sidebar.button("Predict"):
    prediction = model.predict(input_features)
    if prediction[0] == 1:
        st.write("### The model predicts: **Heart Disease**")
    else:
        st.write("### The model predicts: **No Heart Disease**")
