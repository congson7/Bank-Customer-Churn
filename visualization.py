import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def show_visualization(): 

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

    st.title("Customer Data Visualization Unit")


    st.header("1. Customer data")
    data = pd.read_csv("Churn_Modelling.csv")
    st.dataframe(data)

    st.header("2. Proportion of customer churned and retained")
    
    labels = 'Exited', 'Retained'
    sizes = [data.Exited[data['Exited']==1].count(), data.Exited[data['Exited']==0].count()]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
    st.write("Generally, in this dataset, the proportion of clients who continue using their current bank is roughly 80%, while the ratio of those who leave a bank and move to a new one is only 20%. ")


    st.header("3. Geographic Analysis")
    fig1, axarr1 = plt.subplots()
    sns.countplot(x='Geography', hue = 'Exited',data = data)
    st.pyplot(fig1)
    st.write("This dataset only collected data from clients in three countries: France, Germany, and Spain. As we see from the graph, the ratio of clients in France who continue using bank services is the highest with 42%, while the ratio of those who leave the bank is very low, around 8%. We don’t know the exact reasons why French clients remain using bank services, but compared to the statistics in Germany and Spain, this figure is significantly higher.")

    st.header("4. Products Using Analysis")
    fig2, axarr2 = plt.subplots()
    sns.countplot(x='NumOfProducts', hue = 'Exited',data = data)
    st.pyplot(fig2)
    st.write("The more bank’s products clients use, the longer they stay with the bank. In this graph, clients using several bank’s products (specifically 4), have the lowest rate of leaving the bank, only 2,95%. Meanwhile, clients who only use 1 product tend to leave the bank more, with nearly 70%. ")

    
    st.header("5. Credit Card Owner Analysis")
    fig3, axarr3 = plt.subplots()
    sns.countplot(x='HasCrCard', hue = 'Exited',data = data)
    st.pyplot(fig3)
    st.write("Overall, the proportion of clients owning at least one credit card keeping using bank services is higher than those who don’t have any credit card. It can be explained that having a credit card is a factor that keeps clients stay with the bank. The decision to stop using credit cards or change to a new one may be complicated due to the bank’s and client’s procedures.  ")


    st.header("6. Active Member Analysis")
    fig4, axarr4 = plt.subplots()
    sns.countplot(x='IsActiveMember', hue = 'Exited',data = data)
    st.pyplot(fig4)
    st.write("Undoubtedly, clients who are not active members have a higher chance of leaving the bank, around 13%, while it’s 7,35% for those who are active. There are many reasons why they don’t interact and use the bank's products actively, which all lead to the increasing rate of clients leaving the bank.")


    st.header("7. Customer churn per age group")
    fig5, axarr5 = plt.subplots(figsize = (20,15))
    sns.countplot(x='Age', hue = 'Exited',data = data)
    st.pyplot(fig5)
    st.write("Clients at the age of over 40 are the popular age group that decide to leave the bank. As we’ve discussed in the problem statement, this middle-aged group starts having difficulty in approaching new technology, like using high-tech bank products for their transactions. So, they gradually leave a bank with modern technology and may change to a new bank, which provides great offline services. ")