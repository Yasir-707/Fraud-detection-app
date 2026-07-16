import streamlit as st
import pandas as pd
import joblib
model = joblib.load("fraud_detection_pipeline.pkl")
st.title("Fraud detector")
st.markdown("Please enter the transaction details")
st.divider()
transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_IN","CASH_OUT","DEBIT"])
amount = st.number_input("Amount", min_value=0.0,value=1000.0)
oldbalanceOrg = st.number_input("Old Balance(Sender)",min_value=0.0,value=10000.0)
newbalanceOrig = st.number_input("New Balance(Sender)",min_value=0.0,value=9000.0)
oldbalanceDest = st.number_input("Old Balance(Reciever)",min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Balance(Reciever)",min_value=0.0,value=0.0)

if st.button("Predict"):
  input_data = pd.DataFrame([{
      "type" : transaction_type,
      "amount" : amount,
      "oldbalanceOrg" : oldbalanceOrg,
      "newbalanceOrig" : newbalanceOrig,
      "oldbalanceDest" : oldbalanceDest,
      "newbalanceDest" : newbalanceDest
  }])

  prediction = model.predict(input_data)[0]

  st.subheader(f"Prediction:'{int(prediction)}'")

  if prediction == 1:
    st.error("Can be Fraud Transaction")
  else:
    st.success("Looks Like Non-Fraud Transaction")
