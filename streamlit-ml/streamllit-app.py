import streamlit as st
import numpy as np
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Classifier")
st.markdown("Enter flower features below to predict the species:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

# Predict button
if st.button("🔍 Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    species = ["Setosa", "Versicolor", "Virginica"][prediction]
    st.success(f"✅ Predicted Iris Species: **{species}** (Class {prediction})")
