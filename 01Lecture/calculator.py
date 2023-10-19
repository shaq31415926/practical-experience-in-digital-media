# Resource: https://www.askpython.com/python-modules/calculator-app-using-streamlit
import streamlit as st

# add a title to our Calculate App
st.title("Calculator App using Streamlit :book:")

# creates a horizontal line
st.write("---")

# ask the user for input, which is numerical - since we are adding numbers

# input 1
num1 = st.number_input(label="Enter the first number:", step=1, value=7)
# input 2
num2 = st.number_input(label="Enter second number:")

# add mathematical operations
operation = st.radio("Select an operation to perform:",
                     (":heavy_plus_sign:",
                      ":heavy_minus_sign:",
                      ":heavy_multiplication_x:",
                      ":heavy_division_sign:"))

def calculate(num1, num2, operation):
    if operation == ":heavy_plus_sign:":
        total = num1 + num2
    elif operation == ":heavy_minus_sign:":
        total = num1 - num2
    elif operation == ":heavy_multiplication_x:":
        total = num1 * num2
    elif operation == ":heavy_division_sign:" and num2 != 0:
        total = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        total = "Not defined"

    if operation == ":heavy_division_sign:" and num2 == 0:
        pass
    else:
        st.success(f"The total is {total}")

# add the button to calculate
if st.button("Calculate", help= f"Click here to {operation} two numbers"):
    calculate(num1, num2, operation)

