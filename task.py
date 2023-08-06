import os
import time
print("\nNAME = MD. KAMRUZZAMAN")
print("ID = 27 ")
"""
#Task 1: Variable Manipulation
Create two variables, name and age, and assign your name and age to them.
Print out a message like: "My name is [name] and I am [age] years old."
"""

print("\n## Task 1: Variable Manipulation ##")
def name_age (name, age):
    print("\nMy name is " + name +" and I am "+ str(age)+ " years old.")
name=input("\nEnter your name=")
age=input("Enter your age=")
name_age(name, age)    
#time.sleep(5)
#os.system('cls')




"""
Task 2: Data Types and Type Conversion
Create a variable num1 and assign an integer value to it.
Create a variable num2 and assign a float value to it.
Convert num1 to a float and store it in a new variable num1_float.
Convert num2 to an integer and store it in a new variable num2_int.
Print out the types and values of all variables.
"""


print("\n## Task 2: Data Types and Type Conversion ##")
def conversion(num1, num2):
    num1_float= float(num1)
    num2_int=int(num2)
    print("\nInteger number num1 is =" + str(num1) )
    print("Float of  num1 is num1_float= "+ str(num1_float))
    print("\nFloat number num2 is =" + str(num2) )
    print("Integer of  num2 is num2_int= "+ str(num2_int))
num1= int(input("\nEnter a intiger value = "))
num2= float(input("Enter a float value = "))
conversion(num1, num2)    
time.sleep(8)
#os.system('cls')



"""
Task 3: String Manipulation
Create a string variable sentence containing the sentence: "Python programming is fun!"
Print the length of the string.
Print the 8th character (index 7) in the string.
Create a substring from index 0 to 5 and store it in a new variable substring.
Concatenate the substring with the string " I enjoy it!" and print the result.

"""

print("\n## Task 3 : String Manipulation ##")
def string_manipulation():
    #sentence="\"Python programming is fun!\""
    sentence=("Python programming is fun!")
    print("\nThe length of the string = "+ str(len(sentence)))
    print("\n 8th character 8th character (index 7) in the string = " + str(sentence[7]))
    substring=sentence[0:6]
    print("\n I enjoy it! " + substring +"\n")
string_manipulation()    

time.sleep(10)
#os.system('cls')


"""
Task 4: Lists and List Manipulation
Create a list fruits with the following items: "apple", "banana", "cherry", "date".
Add "grape" to the end of the list.Remove "banana" from the list.
Print the length of the list.
Create a new list sliced_fruits containing the second and third items from the fruits list.
Combine sliced_fruits with a new list extra_fruits containing "kiwi" and "lemon". 
Print the combined list.
"""

print("\n## Task 4 : Lists and List Manipulation ##")
def list_manipulation():
    fruits=["apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print("\nAfter add and remove the list = " + str(fruits))
    print("\nThe length of the list = " + str(len(fruits)))
    sliced_fruits=fruits[1:3]
    print("\nThe second and third items from the fruits list = " + str(sliced_fruits))
    extra_fruits=["kiwi", "lemon"]
    combined_fruits=sliced_fruits+extra_fruits
    print("\nThe combined list = " + str(combined_fruits))

list_manipulation()
time.sleep(8)
#os.system('cls')

"""
Task 5: Conditional Statements
Create a variable num and assign an integer value to it.
Write a conditional statement to check if num is even or odd. Print the result.
"""

print("\n## Task 5 : Conditional Statements ##")
def odd_even(num):
    if num%2==0:
        print("\nThe number " + str(num) + " is even\n")
    else:
        print("\nThe number " + str(num) + " is odd\n")
num=int(input("\n Enter an Integer number = "))
odd_even(num)
#time.sleep(5)
#os.system('cls')

"""
Task 6: Loops
Using a loop, print the numbers from 1 to 10.
Using a loop, calculate the sum of numbers from 1 to 100 and print the result.
"""


print("\n## Task 6 : Loops ##")
def loops(n):
    
     s=1
     while s<=n:
        print(s)
        s=s+1
         
n=int(input("\nEnter a positive Integer number 10 = "))
loops(n)   
def summation(n):
    s=1
    sum=0
    while s<=100:
        s=s+1
        sum=sum+s
    print("\nThe sum of numbers from 1 to 100 = "+ str(sum))

n=int(input("\nEnter a positive Integer number 100= "))  
summation(n) 

#time.sleep(5)
#os.system('cls')  

"""
Task 7: Functions
Write a function calculate_square that takes a number as input and returns its square.
Write a function is_prime that takes a number as input and returns whether it's prime or not.
Use the above functions to find and print the square of 7 and check if 29 is prime.
"""
print("\n## Task 7 :  Functions ##")
def calculate_square(n):                                                          
    return n*n
n=int(input("\nEnter  Integer number for square  = "))
sqr=calculate_square(n) 
print("\nThe sqaure of the number is = "+ str(sqr))


def is_prime(num):
    s=1
    for n in range (2,num):
        if num % n==0:
            s=0
            print("\n The number " + str(num) + " is not prime") 
            break;
    return s        

num=int(input("\nEnter  Integer number for prime check = "))
s=is_prime(num)
if s==1:
    print("\n The number " + str(num) + " is  prime") 

time.sleep(5)
#os.system('cls') 

"""
Task 8: Dictionaries
Create a dictionary student with keys "name", "age", and "grade". 
Assign appropriate values.
Add a new key "course" with a value of your choice.
Print all the keys in the dictionary.
Loop through the dictionary and print all key-value pairs.
"""
print("\n## Task 8 : Dictionaries ##")
student=dict()
student['name']="Md Kamruzzaman"
student['age']=33
student['grade']="A-"
student['course']="Web Engineering"
print("\nAll the keys in the student dictionary =", student.keys())
print("\nAll key-value pairs in the dictionary:\n")
for key, value in student.items():
    print(key,":", value)