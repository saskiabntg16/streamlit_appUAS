#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from sklearn import datasets
from sklearn.svm import SVC

model = pickle.load(open('model_uas.pkl', 'rb'))

st.header("SMART INSURANCE")
st.write("NAMA : SASKIA BINTANG MAHARANI")
st.write("NIM : 2019230047")

img = Image.open ('insurance.jpg')
st.image(img, use_column_width=False)
st.write("Please Insert Values, to Insurance prediction:")

st.sidebar.header('Parameter Value Prediction')

age = st.sidebar.slider('age:', 17, 60)
sex = st.sidebar.slider('sex:', 0, 1)
bmi = st.sidebar.slider('bmi',20, 60)
children = st.sidebar.slider('children:', 0, 20)
smoker = st.sidebar.slider('smoker:', 0, 1)
data = {'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children}

features = pd.DataFrame(data, index=[0])

st.subheader('Parameter Inputan')
st.write(features)


# In[ ]:




