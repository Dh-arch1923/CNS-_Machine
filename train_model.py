import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import StandardScaler
import pickle

material_label={0:'Aluminum',1:'Steel',2:'Titanium',3:'Plastic'}
df=pd.read_csv('cnc_machining_dataset.csv')
df.rename(columns={'Estimated_Cost_USD':'Cost'},inplace=True)
df['Volume of Material']=df['Length_mm']*df['Height_mm']*df['Length_mm']
df['Material']=df['Material'].map({'Aluminum':0,'Steel':1,'Titanium':2,'Plastic':3})
x=df.drop(['Cost'],axis=1)
y=df['Cost']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
lr=LinearRegression()
lr.fit(x_train,y_train)
y_predict=lr.predict(x_test)
mae=mean_absolute_error(y_test,y_predict)
mse=mean_squared_error(y_test,y_predict)
rmse=np.sqrt(mse)

with open('model.pkl','wb') as f:
  pickle.dump(lr,f)
with open('material_label.pkl','wb') as f:
  pickle.dump(material_label,f)
print('The model saved successfuly')