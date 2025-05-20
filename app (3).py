# Crete the app and design all the interfaces whichh are required for the end users by using streamlit app

import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

#Now load the model from the pickle that you saved
with open('lr.pkl','rb') as f
   pickle.load(f)

#Now load the model_label that you created into the app
withy open('model_label.pkl','rb) as f:
  pickle.load(f)

#Now set the yitle for your website
st.title('The CnC machine cost predictor')

#Now Design the reauired tabs for the end user
material=st.selectbox('Select the material',('Aluminium','Steel','Titanium','Plastic'))
length=st.number_input('Enter the lenght in(mm)',min_value=0.0)
height=st.number_input('Enter the height in(mm)',min_value=0.0)
width=st.number_input('Enter the width in(mm)',min_value=0.0)
feature_count=st.number_input('Enter the feature count',min_value=0)
cycle_time=st.number_input('Enter the cycle time in(min)',min_value=0.0)

#We can claculate the volume throgh the given input
volume=length*height*width
st.write('The volume of the material is:',volume)

#The user will enter the material name and the model shoul be detect it internally
material_detect={'Aluminium':0,'Steel':1,'Titanium':2,'Plastic':3}
material_encode=material_detect[material]
st.write('The material has been encodeded successfuly')


#Now create a predict button
if st.button('Predict'):
  input_data=np.array([[material_encode,length,height,width,feature_count,cycle_time]])
  prediction=lr.predict(input_data)

  st.success(f"Predicted Cost: ₹{prediction[0]:,.2f}")


