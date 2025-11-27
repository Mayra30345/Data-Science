import numpy as np

#Performing Addition

number=input("Enter the 1st number for performing addition: ")
arr1= np.array([number], dtype=int)
number2=input("Enter the 2nd number for performing addition: ")
arr2= np.array([number2], dtype=int)
result= np.add(arr1, arr2)
print("The addition of two numbers is: ", result)

#Performing Subtraction

number=input("Enter the 1st number for performing substraction: ")
arr1= np.array([number], dtype=int)
number2=input("Enter the 2nd number for performing substraction: ")
arr2= np.array([number2], dtype=int)
result= np.subtract(arr1, arr2)
print("The substraction of two numbers is: ", result)


#Performing Multiplication  
number=input("Enter the 1st number for performing multiplication: ")
arr3= np.array([number], dtype=int)
number2=input("Enter the 2nd number for performing multiplication: ")
arr4= np.array([number2], dtype=int)    
result= np.multiply(arr3, arr4)
print("The multiplication of two numbers is: ", result)

#Performing Division
number=input("Enter the 1st number for performing division: ")                  
arr5= np.array([number], dtype=int)
number2=input("Enter the 2nd number for performing division: ")
arr6= np.array([number2], dtype=int)
result= np.divide(arr5, arr6)
print("The division of two numbers is: ", result)
