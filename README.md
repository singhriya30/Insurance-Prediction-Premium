# Insurance-Prediction-Premium
This project is a Machine Learning–based web application that predicts the insurance premium category of a user based on various personal and lifestyle factors. It integrates a trained ML model with a FastAPI backend and a Streamlit frontend for an interactive user experience.

# Features
Predicts insurance premium category using ML model
FastAPI backend for efficient API handling
Streamlit frontend for user-friendly interface
Real-time prediction based on user inputs
Feature engineering (BMI, age group, lifestyle risk, city tier)

# Tech Stack
Python
FastAPI
Streamlit
Scikit-learn
Pandas & NumPy

# Input Parameters
Age
Weight & Height (for BMI calculation)
Income (LPA)
Smoking habits
City
Occupation

# How It Works
User enters details via Streamlit UI
Data is sent to FastAPI backend
Backend processes features & sends to ML model
Model predicts insurance premium category
Result displayed on UI
