import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("model.pkl", "rb"))
st.title("🌸 Iris Regression App")
st.write("Petal Length predict karein")
sepal_length = st.number_input("Sepal Length (cm)")
sepal_width = st.number_input("Sepal Width (cm)")
petal_width = st.number_input("Petal Width (cm)")
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_width]])
    prediction = model.predict(features)
    
    st.success(f"Predicted Petal Length: {prediction[0]:.2f} cm")