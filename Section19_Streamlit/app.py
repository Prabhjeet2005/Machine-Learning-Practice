import streamlit as st
import pandas as pd
import numpy as np

st.title("This is Title")

st.write("This is Simple Text")

df = pd.DataFrame({
  "First col":[1,2,3,4,45],
  "Second Col":[6,7,8,9,123]
})

st.write("Here is The DataFrame")

# Displaying the Dataframe
st.write(df)

# create a line chart

chart_data = pd.DataFrame(
  np.random.randn(20,3),columns=['Col1','Col2','Col3']
)

st.line_chart(chart_data)
