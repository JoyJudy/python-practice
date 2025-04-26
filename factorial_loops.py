# A python program to find the factorial of a number provided by the user
# using a loop

#define the function that will calculate the factorial
def factorial(y):
    result = 1    # multiplying by 1 doesn't change the result of the number

    if y < 0:    #checks whether the number is a negative
        print("Factorial cannot be negative")
        return None    #stops the function
    elif y == 0:    #checks if the number is zero
        return 1    #the factorial of 0 is 1
    else:
        #using a for loop to multiply the positive integers from 1 upto y
        for i in range(1, y+1):
            result = result * i #multiplies the result by i
        return result    #the final result after the multiplication is done

#request input from the user
n= int(input("Enter number: ")) #convert the input from the user into an integer

#call the function with user input, then printing the result
print(f"Factorial of {n} is {factorial(n)}.")