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
                            icons = ['activity','person-walking','person'],
                            default_index = 0)

#deafult index = 0 means whenever we open the page it will load the page with index 0 here it is Heart Disease Prediction.

#Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction Using ML')

    Age = st.text_input('Age of the Person')
    Sex = st.text_input('Sex of the Person (0-> Female 1-> Male)')
    Cp = st.text_input('Rating of Chest Pain (0 - 3, 3 being severe)')
    testbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Cholestrol level in mg/dl')
    fbs = st.text_input('Fasting blood sugar')
    restecg = st.text_input('Resting Electrocardiographic results (values 0,1,2)')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise induced angina')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    slope = st.text_input('Slope of the Peak Exercise ST segment')
    ca = st.text_input('Number of major vessels (0-3) colored by fluorosopy')
    thal = st.text_input('Thalassemia (0 -> normal, 1 -> fixed defect, 2 -> revarsable defect)')

    #code for Prediction
    heart_pred = ''

    #creating a button for prediction
    if st.button('Heart Disease Result'):
        heart_pred = heart_disease_model.predict([[Age, Sex, Cp, testbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        #reason for 2 square brackets is to tell the model we are predicting for one data point.

        if (heart_pred[0] == 1):
            heart_pred = 'The test returned positive for Heart Disease'
        else:
            heart_pred = 'The test returned negative for Heart Disease'

    st.success(heart_pred)


if(selected == 'Parkinsons Disease Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction Using ML')

if (selected == 'Breast Cancer Prediction'):
    #page title
    st.title('Breast Cancer Prediction')

