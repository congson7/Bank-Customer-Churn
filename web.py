import streamlit as st
import pandas as pd
from prediction import show_prediction
from visualization import show_visualization  
from survey import show_survey



page = st.sidebar.selectbox("",['Survey','Visualization','Prediction'])



if page == 'Survey':
    show_survey()
elif page == 'Visualization': 
    show_visualization()
else:
    show_prediction()