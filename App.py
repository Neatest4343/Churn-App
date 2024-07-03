import streamlit as st
import numpy as np
import joblib

# Load the model using joblib with absolute path
loaded_model = joblib.load('model.joblib')

# Use the model for predictions or further operations

region_to_number = {
   'FATICK': 2, 
   'DAKAR': 0, 
   'LOUGA': 7, 
   'TAMBACOUNDA': 12, 
   'KAOLACK': 4,
   'THIES': 13, 
   'SAINT-LOUIS': 10, 
   'KOLDA': 6, 
   'KAFFRINE': 3, 
   'DIOURBEL': 1,
   'ZIGUINCHOR': 14, 
   'MATAM': 8, 
   'SEDHIOU': 11, 
   'KEDOUGOU': 5, 
   'Other': 9
}
tenure_to_number = {
    '3-6 month' : 0, 
    '6-9 month' : 1, 
    '9-12 month': 2, 
    '12-15 month': 3, 
    '15-18 month': 4, 
    '18-21 month': 5, 
    '21-24 month': 6, 
    '> 24 month': 7
}
yes_churn = 'The client is expected to churn'
no_churn = 'The client is not expected to churn'
default_value = 0.00
def churn_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return no_churn
    else:
        return yes_churn
# give a title to our app
st.title('Welcome to Victor Churn Prediction App')
# Region
REGION = st.selectbox("Region: ", ['Select an option'] + list(region_to_number.keys()) )
TENURE = st.selectbox('Tenure: ', ['Select an option'] + list(tenure_to_number.keys()))
FREQUENCY_RECH = st.number_input("Frequency_Rech:", value=default_value)
REVENUE = st.number_input("Revenue:", value=default_value)
DATA_VOLUME = st.number_input("Data_Volume:", value=default_value)
REGULARITY = st.number_input("Regularity:", value=default_value)
TOP_PACK = st.number_input("Top_Pack:", value=default_value)
try:
    if (st.button('Calculate Churn Probability')):
        # Map the selected option to its corresponding number
        region_number = region_to_number.get(REGION, '')
        tenure_number = tenure_to_number.get(TENURE, '')
        
        try:
            if FREQUENCY_RECH == default_value:
                raise ValueError('to input a value')
            elif REVENUE == default_value:
                raise ValueError('to input a value')
            elif DATA_VOLUME == default_value:
                raise ValueError('to input a value')
            elif REGULARITY == default_value:
                raise ValueError('to input a value')
            elif TOP_PACK == default_value:
                raise ValueError('to input a value')
            result = churn_prediction([FREQUENCY_RECH, REVENUE, DATA_VOLUME, REGULARITY, TOP_PACK, region_number, tenure_number ])
            if result == yes_churn:
                st.error(result)
            else:
                st.success(result)
        except ValueError:
            'Please: Fill all the inputs.'
except ValueError:
    'Please: Fill all the inputs.'
