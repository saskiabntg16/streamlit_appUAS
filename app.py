import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from sklearn import datasets
from sklearn.svm import SVC

# load the model from disk
model = pickle.load(open('model_uas.pkl', 'rb'))

import streamlit as st

# Creating the Titles and Image

st.header("SMART INSURANCE")
st.header("Predict Insurance Charges")
st.write("NAMA : SASKIA BINTANG MAHARANI")
st.write("NIM : 2019230047")

import pandas as pd
def load_data():
    df = pd.DataFrame({'sex': ['Male','Female'],
                       'smoker': ['Yes', 'No']}) 
    return df
df = load_data()

# Take the users input

sex = st.selectbox("Select Sex", df['sex'].unique())
smoker = st.selectbox("Are you a smoker", df['smoker'].unique())
age = st.slider("What is your age?", 18, 100)
bmi = st.slider("What is your bmi?", 10, 60)
children = st.slider("Number of children", 0, 10)

# converting text input to numeric to get back predictions from backend model.
if sex == 'male':
    gender = 1
else:
    gender = 0
    
if smoker == 'yes':
    smoke = 1
else:
    smoke = 0
    
# store the inputs
features = [gender, smoke, age, bmi, children]
# convert user inputs into an array fr the model

int_features = [int(x) for x in features]
final_features = [np.array(int_features)]

if st.button('Predict'):           # when the submit button is pressed
    prediction =  loaded_model.predict(final_features)
    st.balloons()
    st.success(f'Your medical charges would be: ${round(prediction[0],2)}')


