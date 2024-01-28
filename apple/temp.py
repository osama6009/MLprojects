# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st
#from sklearn.neighbors import KNeighborsClassifier

apple_modle = pickle.load(open('C:/Users/welcome/Downloads/trained_model.sav','rb'))


def apple (input_data):
    
    
   input_data_as_numpy_array = np.asarray(input_data)    
   
   input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
   
   prediction = apple.predict(input_data_reshaped)
   
   return (prediction)
   


    
def main():
    
    st.title('apple Quality')
    
    A_id = st.text_input('your id: ')
    Size = st.text_input('input apple size: ')
    Weight = st.text_input('input apple Weight: ')
    Sweetness = st.text_input('input apple Sweetness : ')
    Crunchiness = st.text_input('input apple Crunchiness : ')
    Juiciness = st.text_input('input apple Juiciness : ')
    Ripeness = st.text_input('input apple Ripeness : ')
    Acidity = st.text_input('input apple Acidity : ')
    
    
    dignosis = ''
    # creating a button for perdiction
    if st.button('Result'):
        dignosis = apple([A_id, Size, Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity])


    st.success(dignosis)

if __name__ == '__main__':
    main()    

     
     
   
     
     
     
     
     
     
     
     
