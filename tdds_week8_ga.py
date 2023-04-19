

import streamlit as st
import pandas as pd

st.write("""
# Largest of 3
To find the largest among the 3 given numbers
""")
#Get Input

st.header('Enter 3 numbers')

def user_input_features():
    num1 = st.number_input("num1",min_value=-200000,max_value=200000,step=1)
    num2 = st.number_input("num2",min_value=-200000,max_value=200000,step=1)
    num3 = st.number_input("num3",min_value=-200000,max_value=200000,step=1)
    nums=[num1,num2,num3]
    return (nums)

nums = user_input_features()
output=max(nums)

st.subheader('Largest amongst the 3 is:')
st.write(output)
