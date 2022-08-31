#!/usr/bin/env python
# coding: utf-8

# ## *Import Libraries*

# In[1]:


import streamlit as st
import xgboost as xgb
import numpy as np
import json
from PIL import Image


# ### *Load JSON File*
# 
# We load the JSON file that will help us to preprocess One Hot Encoding data.

# In[2]:


st.cache(allow_output_mutation=True)

def json_file():
    
    with open("columns.json") as columns:
        
        data_json = json.loads(columns.read())
        data_json = np.asarray(data_json['columns_data'])

    return data_json


# ## *User Inputs Widgets*
# 
# We create the widgets so that the user enters the data in a comfortable way.

# In[3]:


st.cache(allow_output_mutation=True)

def UserInputs():
    
    manufacturer = st.selectbox("Manufacturer",("Ford","Toyota","Hyundai","BMW","Audi","Mercedes-Benz"))
    
    if manufacturer == "Ford":
        
        model_car = st.selectbox("Model",('Fiesta', 'Focus', 'Kuga', 'EcoSport', 'C-MAX', 'Ka+',
       'Tourneo Custom', 'S-MAX', 'B-MAX', 'Edge', 'Tourneo Connect',
       'Mondeo', 'KA', 'Grand C-MAX', 'Galaxy', 'Mustang',
       'Grand Tourneo Connect', 'Fusion'))
        
        
    if manufacturer == "Toyota":
        
        
        model_car = st.selectbox("Model",('GT86', 'Corolla', 'RAV4', 'Yaris', 'Auris', 'Aygo', 'C-HR',
       'Prius', 'Avensis', 'Verso', 'Hilux', 'Camry','Land Cruiser'))
    
        
    if manufacturer == "Hyundai":
        
        model_car = st.selectbox("Model",('I20', 'Tucson', 'I10', 'IX35', 'I30', 'I40', 'Ioniq',
       'Kona', 'I800', 'IX20', 'Santa Fe'))
        
        
    if manufacturer == "BMW":
        
        model_car = st.selectbox("Model",('5 Series', '6 Series', '1 Series', '7 Series', '2 Series',
       '4 Series', 'X3', '3 Series', 'X4', 'X1', 'M4', 'X6', 'X5',
       'Z4', 'X7', 'X2', 'M5', 'i8', 'M2', '8 Series', 'M3'))
        
        
    if manufacturer == "Audi":
        
        model_car = st.selectbox("Model",('A1', 'A6', 'A4', 'A3', 'Q3', 'Q5', 'A5', 'Q2', 'A7',
       'RS6', 'Q7', 'A8', 'TT', 'Q8', 'RS4', 'RS5', 'RS3', 'SQ5',
       'S3', 'R8'))
        
        
    if manufacturer == "Mercedes-Benz":
        
        model_car = st.selectbox("Model",('S Class', 'SL CLASS', 'G Class', 'GLE Class', 'GLA Class',
       'GLC Class', 'B Class', 'C Class', 'E Class', 'GL Class',
       'CLS Class', 'A Class', 'SLK', 'V Class', 'CLA Class',
       'CL Class', 'GLS Class', 'M Class', 'X-CLASS'))
    
        
        
        
    trasmission = st.radio('Trasmission',('Automatic','Manual','Semi-Auto'))
    year = st.slider('Year',min_value = 2000,max_value = 2020,step = 1)
    fuelType = st.radio('Fuel Type',('Diesel','Hybrid','Petrol'))
    
    engineSize = st.selectbox('Engine Size',(0.0,1.0, 1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,2.0,2.1,2.2,
       2.3,2.4,2.5,2.8,2.9,3.0,3.5,4.0,4.2,4.4,4.7,5.0,5.2,5.5))
    
    mileage = st.number_input('Mile Age',min_value = 5000,max_value = 74000)
    tax = st.slider('Tax',min_value = 0,max_value = 280,step = 1)
    mpg = st.number_input('MPG',min_value = 20.80,max_value = 250.0)
    
    return manufacturer,model_car,trasmission,year,fuelType,engineSize,mileage,tax,mpg


# ## *One Hot Encoding Preprocessing*

# In[4]:


st.cache(allow_output_mutation=True)

def preprocess():
    
    columns = json_file()
    model_car,manufacturer,trasmision,year,fuelType,engineSize,mileage,tax,mpg = UserInputs()
    
    data = np.zeros(len(columns))
    
    model_idx = np.where(columns == model_car)[0][0]
    trasmision_idx = np.where(columns == trasmision)[0][0]
    fuel_type_idx = np.where(columns == fuelType)[0][0]
    
    data[111] = year
    data[115] = engineSize
    data[116] = mileage
    data[117] = tax
    data[118] = mpg
    
    if model_idx >=0:
        data[model_idx] = 1
        
    if trasmision_idx >=0:
        data[trasmision_idx] = 1
        
    if fuel_type_idx >=0:
        data[fuel_type_idx] = 1
        
    return np.asarray([data])


# ## *Load Model*
# 
# We load the model that we previously trained.So that it takes the user data already processed to be able to generate new predictions.

# In[5]:


st.cache(allow_output_mutation=True)

def predict(new_data):
    model = xgb.XGBRegressor()
    model.load_model("xgb_car_price.json")
    return np.round(model.predict(new_data)).astype(int)


# ## *Generate Predictions*
# 
# The user clicks the "Predict" button to generate the prediction.

# In[6]:


st.cache(allow_output_mutation=True)

def main():
    
    st.subheader("""Predict Price Car""")
    img = Image.open("img.jpeg")
    st.image(img)
  
    new_data = preprocess()
    
    
    if st.button(label = 'Predict'):
        
        price=predict(new_data)
        st.success(f'The estimated price of the vehicle is: $ {price} £')


# In[7]:


st.cache(allow_output_mutation=True)

if __name__ == '__main__':
    main()

