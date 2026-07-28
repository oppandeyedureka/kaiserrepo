#from <filename> import <function_name>
from MathsLibrary import Add, Divide

number1 = input("Enter a numeric value :")
number2 = input("Enter a numeric value :")

try:
    Add(15,"Hello")
except ValueError:
    print("Please mention valid value.")

try:
    Divide(number1, number2)
except ValueError:
    print("Please mention valid value.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")