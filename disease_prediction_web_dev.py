import pickle
import streamlit as st
from streamlit_option_menu import option_menu #used for making the sidebar


#loading the saved models

heart_disease_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\heart_disease_model.sav','rb'))

parkinsons_disease_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\parkinsons_disease_model.sav','rb'))

breast_cancer_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\breast_cancer_model.sav','rb'))

#sidebar for navigation

with st.sidebar:

    selected = option_menu('Select the Desired Disease Prediction Model',
                           ['Heart Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Breast Cancer Prediction'],
                            default_index = 0)

#deafult index = 0 means whenever we open the page it will load the page with index 0 here it is Heart Disease Prediction.

#Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction Using ML')

if(selected == 'Parkinsons Disease Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction Using ML')

if (selected == 'Breast Cancer Prediction'):
    #page title
    st.title('Breast Cancer Prediction')

