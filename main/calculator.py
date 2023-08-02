# Calculator pro 1.0

import math

# Function to add
def fun_add(num1, num2):
    return num1 + num2

# Function for subtraction
def fun_subtraction(num1, num2):
    return num1 - num2

# Function to multiply
def fun_multiply(num1, num2):
    return num1*num2

# Function to divide
def fun_divide(num1, num2):
    if num2 ==0:
        return print("Error! Division by zero not allowed") # Error message when division is attempted with
    else:
        return  float("{0:.3f}".format((float)(num1/num2)))

# Function to do all operations in one
def fun_allInOneEcuation(ecuation):
    
    try:
        result = eval(ecuation)
        return result
    except Exception as e:
        print("ERROR! An unexpected error has occurred", type(e).__name__)
    
    return("ERROR")

