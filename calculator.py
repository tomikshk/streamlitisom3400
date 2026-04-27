
#import streamlit as st

# # Title
# st.title("Basic Web Calculator")

# # Input fields
# num1 = st.number_input("Enter first number", value=0.0)
# num2 = st.number_input("Enter second number", value=0.0)

# # Operation selection
# operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# # Calculate
# if st.button("Calculate"):
#     if operation == "Add":
#         result = num1 + num2
#     elif operation == "Subtract":
#         result = num1 - num2
#     elif operation == "Multiply":
#         result = num1 * num2
#     elif operation == "Divide":
#         result = num1 / num2 if num2 != 0 else "Error: Division by zero"

#     st.success(f"Result: {result}")
    



#Scientific Caluclator (Not optimized)
# import math

# st.header("Scientific Functions")
# operation_sci = st.selectbox("Choose scientific operation", ["Square Root", "Power", "Sin", "Cos", "Tan"])

# value = st.number_input("Enter value", value=0.0)
# power = st.number_input("Enter power (if applicable)", value=2.0)

# if st.button("Calculate Scientific"):
#     if operation_sci == "Square Root":
#         result = math.sqrt(value)
#     elif operation_sci == "Power":
#         result = math.pow(value, power)
#     elif operation_sci == "Sin":
#         result = math.sin(math.radians(value))
#     elif operation_sci == "Cos":
#         result = math.cos(math.radians(value))
#     elif operation_sci == "Tan":
#         result = math.tan(math.radians(value))

#     st.success(f"Result: {result}")

import streamlit as st
import math

st.header("Scientific Functions")

operation_sci = st.selectbox(
    "Choose scientific operation",
    ["Square Root", "Power", "Sin", "Cos", "Tan"]
)

# Show inputs only when relevant
if operation_sci == "Power":
    value = st.number_input("Enter base", value=0.0)
    power = st.number_input("Enter exponent", value=2.0)
elif operation_sci == "Square Root":
    value = st.number_input("Enter value (must be ≥ 0)", value=0.0)
else:  # Sin, Cos, Tan
    value = st.number_input("Enter angle (in degrees)", value=0.0)

if st.button("Calculate"):
    try:
        if operation_sci == "Square Root":
            if value < 0:
                st.error("Cannot take square root of a negative number.")
            else:
                st.success(f"√{value} = {math.sqrt(value):.6f}")
        elif operation_sci == "Power":
            st.success(f"{value} ^ {power} = {math.pow(value, power):.6f}")
        elif operation_sci == "Sin":
            st.success(f"sin({value}°) = {math.sin(math.radians(value)):.6f}")
        elif operation_sci == "Cos":
            st.success(f"cos({value}°) = {math.cos(math.radians(value)):.6f}")
        elif operation_sci == "Tan":
            if value % 180 == 90:
                st.error("tan(90°) is undefined.")
            else:
                st.success(f"tan({value}°) = {math.tan(math.radians(value)):.6f}")
    except Exception as e:
        st.error(f"Error: {e}")
