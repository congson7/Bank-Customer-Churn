import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

pip install sklearn

def load_model():
    with open('save_step.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rf_loaded = data["model"]
label_gender = data["label_gender"]
label_geography = data["label_geography"]


def show_prediction():
    page_bg_img = """
    <style>
    [data-testid = "stAppViewContainer"]{
        background-color: #fff;
        background-image:
        linear-gradient(90deg, transparent 79px, #abced4 79px, #abced4 81px, transparent 81px),
        linear-gradient(#eee .1em, transparent .1em);
        background-size: 100% 1.2em;
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html = True)


    st.title("Customer Churn Prediction Unit")

    Age = st.slider("Enter your age",0,120,1)



    col1, col2, col3 = st.columns(3)
    CreditScore = col3.number_input("What is your credit score ?")
    Geography = col1.selectbox("Where are you from ?",["France","Germany","Spain"])
    Gender = col1.selectbox("Enter your gender",["Male","Female"])
    Tenure = col2.slider("What is your tenure ?",0,10,1)
    Balance = col3.number_input("What is your bank balance ?")
    NumOfProducts = col1.number_input("How many product you use?")
    HasCrCard = col2.radio("Do you have credit card ?",[1,0])
    IsActiveMember = col2.radio("Is you a active member ?",[1,0])
    EstimatedSalary = col3.number_input("What is your estimated salary ?")

    
    



    ok = st.button("Predict")

    if ok : 

        X = np.array([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])
        X[:, 1] = label_geography.fit_transform(X[:, 1])
        X[:, 2] = label_gender.fit_transform(X[:, 2])
        X = X.astype(float)

        existed = rf_loaded.predict(X)
        
        if (existed == 0):
            st.write('<p class="big-font">This customer is likely will not leave a bank.</p>',unsafe_allow_html=True)
        else:
            st.write('<p class="big-font">This customer is likely to leave a bank.</p>',unsafe_allow_html=True)

