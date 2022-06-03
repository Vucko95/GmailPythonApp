import streamlit as st
import pandas

data = {
    'Series_1': [1, 2, 3, 4, 5],
    'Series_2': [10, 20, 30, 40, 50]
}
dataframe = pandas.DataFrame(data)
st.title('My App')
st.subheader("This is a Subheader")
st.write("This is a test WebApp")
st.write(dataframe)
st.line_chart(dataframe)
st.area_chart(dataframe)
st.slider("Testing")
