#create a function and pass in users input as a parameter
#if number is less than one use print function to mean negative
#if number is more than one print positive
#if number is one
print("This is a programme that tells if a number is positive or negative")
def number_check(p):
    numb=int(input("Enter a number "))
    if numb<1:
        print(f"{numb} is  a negative  number")
    elif numb>1:
        print(f"{numb} is a positive number")
    else:
        print("Good job!That is a whole number")
#Request for users input #
#Create a function and pass a parameter
#Request for user input and equate it to parameter
#create a variable and assign it 1
#loop through each number using range function of the parameter
#Multiply each and assign it to varable.
#End function
def factorial(a):
    a=int(input("Enter a number"))
    p=1
    # range(1,a+1) error int object is not iterablr
    for num in range(1,a+1):
        p*=num
    print(f"Factorial of {a} is {p}")
    
        