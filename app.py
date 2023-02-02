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
    st.markdown('Oleh : Putri Dita Pratiwi (2019230001) | UAS Datamining')
    st.write('\n')
    st.markdown('Silakan isi form berikut terlebih dahulu :')
    
    st.write('\n')
    age = st.number_input("Age", 0)
    sex = st.number_input("Sex (Male = 0, Female = 1)", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker (Yes = 1, No = 0)", 0)
    result =""
    
    if st.button("PREDIKSI"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Charges {}'.format(result))
    
if __name__=='__main__':
    main()
