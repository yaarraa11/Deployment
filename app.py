import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    with open ('saved_steps.pkl', 'rb') as file:
        data = pickle.load(data, file)
    return data
    


data = load_model()

stacked = data["model"]
rob_scaler = data["scaler"]
columns = ['Class', 'scaled_amount', 'scaled_time','V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11',
       'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21',
       'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

def show_predict_page():
    st.title("credit card fraud detection Prediction ")

    st.write("""### We need some information for prediction""")

    scaled_amount = (0,1)
    

    scaled_time = ( 0 , 1)

                   


   

    scaled_amount = st.selectbox("Amount", scaled_amount)
    scaled_time = st.selectbox("Time", scaled_time)
   

    ok = st.button("Predict")

   

    if ok:
        X = np.array([[ Class, scaled_amount, scaled_time ,V1 , V2 , V3 , V4, V5, V6, V7, V8, V9, V10, V11,
               V12, V13, V14, V15, V16, V17, V18, V19, V20, V21,
               V22, V23, V24, V25, V26, V27, V28 ]])
        X = pd.DataFrame(scaler.transform(X), columns=columns)

        prediction = stacked.predict(X)

        if prediction == 1:
            prediction = "Fraud"
        else:
            prediction = "Not Fraud"
            
        st.subheader(f"Is the transaction fraudulent? \n {prediction}")


show_predict_page()