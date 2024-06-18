
import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World")
st.write("## This is H2 Title")
x = st.text_input("Movies", "Star wars")
if st.button("click me"):
    st.write(f"your favourite movie is :'{x}'")

data = pd.read_csv("movies.csv")
chart_data = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])

st.write(f"favourite movie is :{x}")
st.write("data")

st.bar_chart(chart_data)
