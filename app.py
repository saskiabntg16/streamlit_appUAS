import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle #to load a saved model

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def prediction(age, sex, bmi, children, smoker):

    prediction = nb.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.write('Nama : Saskia Bintang Maharani')
    st.write('NIM : 2019230047')
    st.write('\n')
    st.title('Pembayaran Premi Asuransi :') 
    st.write('\n')
    st.write('\n')
    img = Image.open ('insurance.jpg')
    st.image(img, use_column_width=False)
    st.title("Aplikasi Prediksi Pembayaran Premi Asuransis Dengan Algoritma Regresi Linier")
    st.markdown('Dataset :')
    data=pd.read_csv('insurance1.csv')
    st.write(data.head())

elif app_mode == 'Prediction':
    st.write('\n')
    st.write('Nama : Saskia Bintang Maharani')
    st.write('Nim : 2019230047')
    st.write('\n')
    st.title('Isi Data Dibawah Ini :')
    
    st.write('\n')
            age = st.number_input("Age", 0)
    sex = st.number_input("Sex (Male = 0, Female = 1)", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker (Yes = 1, No = 0)", 0)
    result =""
    

    
    if st.button("Pedict"):
        result = prediction(age, sex, bmi, children, smoker)

    st.success('Hasil Prediksi Dengan Algoritma Regresi Linier = {}'.format(result))
