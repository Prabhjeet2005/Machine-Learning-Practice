import pandas as pd
import streamlit as st

st.write("Enter Name: ")
name = st.text_input("Enter Here")

age = st.slider("Enter Your Age",0,100,19)

options = ["Python","C++","JavaScript"]
choice = st.selectbox("Select Your Favourite Language",options)

if name and age:
  st.write(f"Hi {name} your Age is {age} Favourite Language: {choice}")

data = {
  "Name":["Prabhjeet","Raman"],
  "Age":[19,20],
  "City":["Delhi","Mumbai"]
}

df = pd.DataFrame(data)

st.write(df)
df.to_csv("SampleData.csv")

fileupload = st.file_uploader("Upload CSV File Here",type="csv")

if fileupload is not None:
  df1 = pd.read_csv(fileupload)
  st.write(df1)
