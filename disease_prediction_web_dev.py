import pickle
import streamlit as st
from streamlit_option_menu import option_menu #used for making the sidebar


#loading the saved models

heart_disease_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\heart_disease_model.sav','rb'))

parkinsons_disease_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\parkinsons_disease_model.sav','rb'))

breast_cancer_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\breast_cancer_model.sav','rb'))

diabetes_prediction_model = pickle.load(open(r'C:\Users\kenneth\OneDrive\Desktop\Disease Prediction\Disease-Prediction\saved_models\diabetes_prediction_model.sav', 'rb'))

#sidebar for navigation

with st.sidebar:

    selected = option_menu('Select the Desired Disease Prediction Model',
                           ['Heart Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Breast Cancer Prediction',
                            'Diabetes Prediction'],
                            default_index = 0)

#deafult index = 0 means whenever we open the page it will load the page with index 0 here it is Heart Disease Prediction.

#Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')
    try:

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
        ca = st.text_input('Number of major vessels (0-4) colored by fluorosopy')
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
    except ValueError as e:
        st.error(f"Invalid Input. Please enter a numeric value. Error: {e}")


if(selected == 'Parkinsons Disease Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction using ML')

    Fo = st.text_input('Enter the MDVP: Fo(Hz) value')
    Fhi = st.text_input('Enter the MDVP:Fhi(Hz) value')
    Flo = st.text_input('Enter the MDVP:Flo(Hz) value')
    Jitter_perc = st.text_input('Enter the MDVP:Jitter(%) value')
    Jitter_abs = st.text_input('Enter the MDVP:Jitter(Abs) value')
    Rap = st.text_input('Enter the MDVP:RAP value')
    ppq = st.text_input('Enter the MDVP:PPQ value')
    Jitter_ddp = st.text_input('Enter the Jitter:DDP value')
    Shimmer = st.text_input('Enter the MDVP:Shimmer value')
    Shimmer_dB = st.text_input('Enter the MDVP:Shimmer(dB) val')
    Shimmer_APQ3 = st.text_input('Enter the Shimmer:APQ3 value')
    Shimmer_APQ5 = st.text_input('Enter the Shimmer:APQ5 value')
    apq = st.text_input('Enter the MDVP:APQ value')
    dda = st.text_input('Enter the Shimmer:DDA value')
    nhr = st.text_input('Enter the NHR value')
    hnr = st.text_input('Enter the value HNR value')
    rpde = st.text_input('Enter the RPDE value')
    dfa = st.text_input('Enter the DFA value')
    spread1 = st.text_input('Enter the spread1 value')
    spread2 = st.text_input('Enter the spread2 value')
    D2 = st.text_input('Enter the D2 value')
    ppe = st.text_input('Enter the PPE value')

    parkinson_pred = ''

    #code for Prediction
    if st.button('Parkinson Disease Result'):
        try:
            parkinson_pred = parkinsons_disease_model.predict([[Fo, Fhi, Flo, Jitter_perc, Jitter_abs, Rap, ppq, Jitter_ddp, Shimmer, Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, D2, ppe]])

            if (parkinson_pred[0] == 0):
                parkinson_pred = "The Patient is tested negative for Parkinson Disease"
            else:
                parkinson_pred = "The Patient is tested positive for Parkinson's Disease"

            st.success(parkinson_pred)
        except ValueError as e:
            st.error(f"Invalid Input. Please enter numeric values. Error: {e}")




if (selected == 'Breast Cancer Prediction'):
    #page title
    st.title('Breast Cancer Prediction using ML')
    try:

        radius_mean = st.text_input('Enter the mean radius')
        texture_mean = st.text_input('Enter the mean texture')
        perimeter_mean = st.text_input('Enter the mean perimeter')
        area_mean = st.text_input('Enter the mean area')
        smoothness_mean = st.text_input('Enter the mean smoothness')
        compactness_mean = st.text_input('Enter the mean compactness')
        concavity_mean = st.text_input('Enter the mean concavity')
        concavity_mean_points = st.text_input('Enter the mean concavity points')
        symmetry_mean = st.text_input('Enter the mean symmetry')
        fractal_dimension_mean = st.text_input('Enter the mean fractional dimension')
        radius_se = st.text_input('Enter the radius error')
        texture_se = st.text_input('Enter the texture error')
        perimeter_se = st.text_input('Enter the perimeter error')
        area_se = st.text_input('Enter the area error')
        smoothness_se = st.text_input('Enter the smoothness error')
        compactness_se = st.text_input('Enter the compactness error')
        concavity_se = st.text_input('Enter the concavity error')
        concave_points_se = st.text_input('Enter the concave points error')
        symmetry_se = st.text_input('Enter the symmetry error')
        fractal_dimension_error = st.text_input('Enter the fractional dimension error')
        radius_worst = st.text_input('Enter the worst radius')
        texture_worst = st.text_input('Enter the worst texture')
        perimeter_worst = st.text_input('Enter the worst perimeter')
        area_worst = st.text_input('Enter the worst area')
        smoothness_worst = st.text_input('Enter the worst smoothness')
        compactness_worst = st.text_input('Enter the worst compactness')
        concavity_worst = st.text_input('Enter the worst concavity')
        concavity_points_worst = st.text_input('Enter the worst concavity points')
        symmetry_worst = st.text_input('Enter the worst symmetry')
        fractal_dimension_worst = st.text_input('Enter the worst fractional dimension')

        breast_cancer_pred = ''

        if st.button('Breast Cancer Result'):
            breast_cancer_pred = breast_cancer_model.predict([[float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean), float(smoothness_mean), float(compactness_mean), float(concavity_mean), float(concavity_mean_points), float(symmetry_mean), float(fractal_dimension_mean), float(radius_se), float(texture_se), float(perimeter_se), float(area_se), float(smoothness_se), float(compactness_se), float(concavity_se), float(concave_points_se), float(symmetry_se), float(fractal_dimension_error), float(radius_worst), float(texture_worst), float(perimeter_worst), float(area_worst), float(smoothness_worst), float(compactness_worst), float(concavity_worst), float(concavity_points_worst), float(symmetry_worst), float(fractal_dimension_worst)]])

            if (breast_cancer_pred[0] == 0):
                breast_cancer_pred = 'Negative for Breast Cancer'
            else:
                breast_cancer_pred = 'Positive for Breast Cancer'

            st.success(breast_cancer_pred)
    except ValueError as e:
        st.error(f"Invalid Input. Please enter numeric values. Error: {e}")


if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')

    try:

        Age = st.text_input('Enter your age')
        gender = st.text_input('Enter your gender')
        hypertension = st.text_input('Enter hypertension')
        heart_disease = st.text_input('presence of heart disease')
        smoking_history = st.text_input('smoking history (0 -> current, 1 -> former, 2 -> never)')
        bmi = st.text_input('Enter your BMI value')
        HbA1c_level = st.text_input('Enter your HbA1c level')
        blood_glulcose = st.text_input('Enter your blood glucose level')

        diabetes_pred = ''
        if st.button('Diabetes Prediction Result'):
            diabetes_pred = diabetes_prediction_model.predict([[Age, gender, hypertension, heart_disease,smoking_history, bmi,HbA1c_level, blood_glulcose]])

            if (diabetes_pred[0] == 0):
                diabetes_pred = 'Negative for Diabetes'
            else:
                diabetes_pred = 'Positive for Diabetes'

            st.success(diabetes_pred)
    except ValueError as e:
        st.error(f"Invalid input. Please enter numeric values. Error: {e}")







