#A python program that finds the factorial of a number provided by a user
#using recursion

#define a function that will compute the factorial using recursion
def factorial(y):

    #first, we check whether the number is a negative integer, zero, or positive integer
    if y < 0:    #checks if number is a negative
        print("Factorial cannot be negative")
    elif (y == 0 or y==1):    #checks if number is zero or 1 (base case since the factorial of both 0 and 1 is 1)
        return 1
    else:    #checks if the number is greater than zero
        return y * factorial(y - 1)   #the recursive case now when the number is greater than 0

#request for user input
num = int(input("Enter a number: "))

#call the function, and print the solution
print(f"The factorial of {num} is {factorial(num)}. ")




