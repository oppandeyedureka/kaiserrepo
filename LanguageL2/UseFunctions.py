#create functions

#Global Variable
resultvalue = 1000

#function definition
def func1():
    print("Welcome to Functions!")

#functions with input parameters and return values
def add(num1, num2):
    global resultvalue
    #local variable Or Function level variable
    result = int(num1)+int(num2)
    print("Global value inside function", resultvalue)
    resultvalue = 1500
    print("Global value inside function", resultvalue)
    print("Sum is : ", result)
    return result

#Pass Function parameters
add(12,34)
print(add(12,45))
#print(result)#Error result is a local variable
resultvalue = 1200
print("Global Value outside function", resultvalue)#accessing a Global Variable