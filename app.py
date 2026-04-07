import streamlit as st
import pickle

st.title("Weather Prediction App")
pn=st.number_input("enter precipitaion")
maxt=st.number_input("enter maximum temperature")
mint=st.number_input("enter minimum temperature")
wind=st.number_input("enter wind speed")
button=st.button("predict!")

if button:
  lr=pickle.load(open("wp.pkl","rb"))
  res=lr.predict([[pn,maxt,mint,wind]])[0]
  st.markdown(f"today weather situation: {res}")

