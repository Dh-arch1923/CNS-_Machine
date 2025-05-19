import streamlit as st
import pickle

#Save the model
with open('model.pkl','rb') as f:
  model=pickle.load(f)
#Save the material label
with open('material_label.pkl','rb') as f:
  material_label=pickle.load(f)

#Creat the material as  drodown list whicg will be helpful for the user
material_options={x:m for m,x in material_label.items()}

#Set the title of the userinterface
st.title('CNC Machine Cost Predection')

#Dropdown for the Material
material_name=st.selectbox('Material',list(material_label.keys()))
materials=material_label[material_name]

#Input fields
length=st.number_input('Length (mm)',min_value=0.0)
height=st.number_input('Height (mm)',min_value=0.0)
width=st.number_input('Width (mm)',min_value=0.0)
feature_count=st.number_input('Feature Count',min_value=0)
cycle_time=st.number_input('Cycle Time (min)',min_value=0.0)

#Calculate the volume
volume=length*height*width
st.write(f"Calculated volume is: {volume:.2f}mm³")

#Predict button
if st.button('Predict'):
  input_data=np.array([[materials,length,height,width,feature_count,cycle_time,volume]])
  prediction=model.predict(input_data)
  st.write(f"Predicted Cost: ${prediction[0]:.2f}")