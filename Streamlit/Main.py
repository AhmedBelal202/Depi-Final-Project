import streamlit as st
def convert_to_str(x):
    return str(x)
st.set_page_config(
    page_title="Store Sales Forecasting",  # <- Change this title
    page_icon="📊",                         # Optional emoji or icon
    layout="wide"                           # Use 'centered' or 'wide'
)

# Main page title
st.title("📌 Rossmann Store Sales Forecasting: Problem & Solution")

# Sidebar info for this page
st.sidebar.header("ℹ️ Problem Overview")
st.sidebar.info("""
This page outlines the main business problem and the data science solution applied to forecast store sales in the Rossmann challenge.
""")

# Introduction
st.header("📍 Problem Definition")
st.markdown("""
Rossmann, one of Europe’s largest drugstore chains, operates over **3,000 stores in 7 countries**, with **1,115 stores in Germany** alone.

Store managers must forecast **daily sales up to six weeks in advance**. These forecasts are essential for:

- 📦 **Inventory control**
- 👥 **Staff scheduling**
- 📈 **Operational efficiency**

However, sales are affected by many dynamic factors such as:

- Promotional campaigns  
- Local competition  
- School and state holidays  
- Store location and demographics  
- Seasonality and trends  

To address this challenge, Rossmann hosted a **Kaggle competition** aimed at building a robust machine learning model for **daily sales forecasting**.
""")

# Project Goals
st.header("🎯 Project Objectives")
st.markdown("""
1. **Analyze and explore** the Rossmann dataset (sales, promotions, holidays, stores).
2. **Identify important factors** influencing sales performance.
3. **Preprocess and clean** the data for use in machine learning models.
4. **Build forecasting models** such as:
   - Linear Regression  
   - Decision Trees  
   - Random Forest  
   - XGBoost  
   - LSTM (for time series)
5. **Evaluate models** using metrics like **RMSE** or **MAE**.
6. **Optimize** the best model with hyperparameter tuning.
7. **Deliver insights** and recommendations to support better planning and store-level decision-making.
""")

# Methodology
st.header("🛠️ Project Methodology")
st.markdown("""
- **Exploratory Data Analysis (EDA):**  
  Identify patterns and visualize sales drivers.

- **Data Preprocessing:**  
  Encode categories, handle missing values, and create useful features like weekday/holiday flags.

- **Modeling:**  
  Test multiple models, optimize performance, and validate results.

- **Evaluation:**  
  Compare models using hold-out data and key metrics.

- **Insights & Reporting:**  
  Share practical recommendations for improving sales strategy.
""")

st.success("✅ This project demonstrates how machine learning can improve retail forecasting and guide smarter business decisions.")

