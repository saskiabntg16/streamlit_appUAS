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
        sex = st.selectbox("Select Sex", df['sex'].unique())
        smoker = st.selectbox("Are you a smoker", df['smoker'].unique())
        age = st.slider("What is your age?", 18, 100)
        bmi = st.slider("What is your bmi?", 10, 60)
        children = st.slider("Number of children", 0, 10)
        
            if sex == 'male':
                gender = 1
            else:
                gender = 0

            if smoker == 'yes':
                smoke = 1
            else:
                smoke = 0
    result =""
    

    
    if st.button("Pedict"):
        result = prediction(sex, smoker, age, bmi, children)
    st.success('Hasil Prediksi Dengan Algoritma Regresi Linier = {}'.format(result))
