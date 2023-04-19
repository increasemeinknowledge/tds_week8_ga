import streamlit as st
import pandas as pd

st.write("""
# Largest of 3 numbers
This app tells the largest number out of three
""")
#Get Input

st.header('Enter 3 numbers')

def user_input_features():
   num1 = float(input())
   num2 = float(input())
   num3 = float(input())

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3



nums = user_input_features()
output=largest

st.subheader('Maximum amongst the 3 is:')
st.write(output)
