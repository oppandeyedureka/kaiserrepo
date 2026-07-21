name = "Omprakash"
print("Type is ", type(name))
age = "40"
print("Type is ", type(age))
new_age = 40
print("Type is ", type(new_age))
insured = True
print("Type is ", type(insured))
insurance_amount = 5000.50
print("Type is ", type(insurance_amount))

#Type casting or Conversion
print(int(age) + new_age) #This will give an error as age is a string and new_age is an integer

"""
user_age = int(input("Enter your age: "))
print("Your age is: ", user_age)

user_salary = float(input("Enter your salary: "))
print("Your salary is: ", user_salary, type(user_salary))
"""

user_insured = bool(input("Are you insured? (True/False): "))
print("Are you insured? ", user_insured, type(user_insured))

complex_number = 30 + 5j
print("Type is ", type(complex_number))