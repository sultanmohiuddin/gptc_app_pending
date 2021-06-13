# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:52:18 2021

@author: user
"""

import streamlit as st
import pandas as pd
from PIL import Image


st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('welcome to GPTC Data visulization app')
st.header('please upload file to get started')
st.sidebar.subheader('visulization settings') 
image = Image.open('C:\\Users\\user\\Desktop\gptc_logo.PNG')
st.sidebar.image(image, caption='')
uploaded_file=st.sidebar.file_uploader(label='upload your csv or exel file',type=['csv','xlsx'])

global myfile
if uploaded_file is not None:
    myfile=pd.read_csv(uploaded_file)
    st.write(myfile)
    
chart_types=['Bar','Area','line']
choice=st.sidebar.selectbox('select chart',chart_types)


try:
    
    if choice == 'line':
         st.line_chart(myfile)
   
        
    elif choice == 'Bar':
        st.bar_chart(myfile)
 
    
    elif choice == 'Area':
         st.area_chart(myfile)
    else:
          print('no file is selected')
          
except:
    print('something is worng')
  
  
     



     
  
      
     

      


   
   


    


    




        


    
 
     
   
       


