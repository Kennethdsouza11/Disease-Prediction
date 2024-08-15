
# Multiple Disease Prediction System

This project aims to provide a comprehensive disease prediction system for several conditions using machine learning models. The models include predictions for breast cancer, heart disease, Parkinson's disease, and diabetes. The system is implemented with an interactive user interface built using Streamlit.

## Table of Contents

1. Project Overview
2. Models Used
3. Hyperparameter Tuning
4. User Interface
5. Usage

## Project Overview

This project provides a predictive system for multiple diseases. Users can input various health metrics through an interactive web interface, and the system will predict the likelihood of having a specific condition. The project uses machine learning models to achieve this, offering a practical tool for health assessments.

## Models Used

1. Breast Cancer Prediction:
- >Model: Logistic Regression
- >Description: Predicts the likelihood of breast cancer based on various features such as radius, texture, and area.

2. Heart Disease Prediction:

- >Model: Support Vector Classifier (SVC)
- > Description: Predicts the likelihood of heart disease based on patient data.

3. Parkinson's Disease Prediction:

- > Model: Support Vector Classifier (SVC)
- > Description: Predicts the likelihood of Parkinson's disease based on features from the health metrics

4. Diabetes Prediction:

- >Model: Support Vector Classifier (SVC)
- >Description: Predicts the likelihood of diabetes based on patient health metrics.

## Hyperparameter Tuning

For the SVC models used in heart disease, Parkinson's disease, and diabetes predictions, hyperparameter tuning was performed to optimize model performance. The following hyperparameters were tuned:

- >C (Regularization parameter)
- >kernel (Kernel type to be used in the algorithm)
- >gamma (Kernel coefficient for ‘rbf’, ‘poly’, and ‘sigmoid’ kernels)
- >degree (Degree of the polynomial kernel function)
Tuning was done using Grid Search and Randomized Search techniques to find the best combination of these parameters.

## User Interface

The interactive user interface is built using Streamlit. It allows users to input their health metrics and receive predictions for the following conditions:

- >Breast Cancer
- >Heart Disease
- >Parkinson's Disease
- >Diabetes

## Installation

### Prequisites

- >Python 3.x installed on your system
- >Ensure you have 'pip' installed

### Steps

1. Clone this repository:
- >     git clone https://github.com/your-username/multiple-disease-prediction.git
- >     cd multiple-disease-prediction
2. Create and activate a virtual environment (optional but recommended):
- >     python -m venv venv
- >     source venv/bin/activate (on Windows: venv\Scripts\activate)
3. Install the require packages
- >     pip install -r requirements.txt
4. Run the Streamlit app:
- >     streamlit run disease_prediction_web_dev.python
5. Open your browser and navigate to your local host to view the application.
## Usage

1. Open your web browser and navigate to the URL provided by Streamlit
2. Select the type of disease prediction you want to perform.
3. Input the required health metrics into the text fields.
4. Click the 'Predict' button to get the prediction result.
