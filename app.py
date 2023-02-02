import streamlit as st
import pandas as pd
import numpy as np
import pickle #to load a saved model

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def prediction(age, sex, bmi, children, smoker):

    prediction = nb.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.write('Nim : 2019230039')
    st.write('Nama : Esa Meytha Shamirah')
    st.write('\n')
    st.title('Pembayaran Premi Asuransi :') 
    st.write('\n')
    st.write('\n')
    st.image('insurance.jpg')
    st.title("Aplikasi Prediksi Pembayaran Premi Asuransis Dengan Algoritma Regresi Linier")
    st.markdown('Dataset :')
    data=pd.read_csv('insurance1.csv')
    st.write(data.head())

elif app_mode == 'Prediction':
    st.write('\n')
    st.write('Nim : 2019230039')
    st.write('Nama : Esa Meytha Shamirah')
    st.write('\n')
    st.title('Silakan, isi form berikut ini :')
    
    st.write('\n')
    age = st.number_input("Age", 0)
    sex = st.number_input("Sex (Male = 0, Female = 1)", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker (Yes = 1, No = 0)", 0)
    result =""
    
    if st.button("SUBMIT"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Hasil Prediksi Dengan Algoritma Regresi Linier = {}'.format(result))

    st.success('Hasil Prediksi Dengan Algoritma Regresi Linier = {}'.format(result))
