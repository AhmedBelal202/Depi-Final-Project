import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Define function to convert columns to string
def convert_to_str(value):
    return str(value)

# Set page config
st.set_page_config(page_title="Sales Prediction App", page_icon="📊")

# Get absolute path to the model file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'finalized_model.sav')

# Load the model safely
model = None
if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}")
else:
    try:
        model = joblib.load(model_path)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")

# App title efficace
st.title("📊 Sales Prediction App")

# Sidebar content
st.sidebar.header("🛠️ App Info")
st.sidebar.info("""
This app uses a machine learning model to predict store sales based on store attributes.
Please fill in the store details in the form on the right, then click **Predict Sales** to get the forecast.
""")

st.write("📝 Fill in the store details to predict expected sales.")

# Input form
col1, col2 = st.columns(2)

with col1:
    store_type = st.selectbox("Store Type", ['a', 'b', 'c', 'd'])
    assortment = st.selectbox("Assortment Type", ['a', 'b', 'c'])
    competition_distance = st.text_input("Competition Distance", "500.0")
    competition_year = st.number_input("Competition Open Since Year", min_value=1900, max_value=2025, value=2010)
    competition_month = st.number_input("Competition Open Since Month", min_value=0, max_value=12, value=6)

with col2:
    promo2 = st.selectbox("Is Promo2 Active?", [0, 1])
    promo2_year = st.number_input("Promo2 Start Year", min_value=1900, max_value=2025, value=2013)
    promo2_week = st.number_input("Promo2 Start Week", min_value=0, max_value=52, value=20)
    promo_interval = st.text_input("Promo Interval (e.g. Feb,May,Aug,Nov)", "Feb,May,Aug,Nov")

# When the button is clicked
if st.button("Predict Sales"):
    if model is None:
        st.error("Cannot predict: Model not loaded successfully.")
    else:
        try:
            # Prepare the input data as a DataFrame
            input_data = pd.DataFrame([{
                'StoreType': store_type,
                'Assortment': assortment,
                'CompetitionDistance': competition_distance,
                'CompetitionOpenSinceMonth': competition_month,
                'CompetitionOpenSinceYear': competition_year,
                'Promo2': promo2,
                'Promo2SinceWeek': promo2_week,
                'Promo2SinceYear': promo2_year,
                'PromoInterval': promo_interval
            }])

            # Make predictions with the model
            prediction = model.predict(input_data)

            # Display the predicted sales result
            st.markdown(
                f"""
                <div style='
                    font-size: 48px;
                    font-weight: bold;
                    color: #2E8B57;
                    margin: 30px 0px 30px 0px;
                    text-align: center;
                    '>
                    Predicted Sales 🧠💡: {prediction[0]:,.2f}
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")
