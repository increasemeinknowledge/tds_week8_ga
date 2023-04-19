import streamlit as st

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the Largest Number")
st.write("Enter three numbers below to find the largest among them.")

# Create input fields for three numbers
a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

# Call the find_largest function to get the largest number
largest = find_largest(a, b, c)

# Display the result
st.write(f"The largest number among {a}, {b}, and {c} is {largest}.")
