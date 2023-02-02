import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def welcome():
    return 'Selamat Datang'

def prediction(age, sex, bmi, children, smoker):

    prediction = nb.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

def main():
    st.title("Aplikasi Prediksi Asuransi dengan Algoritma Linier Regression")
    st.markdown('Nama : Saskia Bintang Maharani | NIM : 2019230047')
    st.write('\n')
    st.markdown('Silakan isi form berikut terlebih dahulu :')
    
    st.write('\n')
    age = st.number_input("Age", 0)
    sex = st.number_input("Sex (Laki-Laki = 0, Perempuan = 1)", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker (Smoker = 1, Non Smoker = 0)", 0)
    result =""
    
    if st.button("Predict"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Hasil Prediksi Dengan Algoritma Regresi Linier {}'.format(result))
    
if __name__=='__main__':
    main()
