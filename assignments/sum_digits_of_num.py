# A python program that finds the sum of the digits of a number

#define the function that will calculate the sum of the digits
#it takes the number y
def sum_digits(y):
    total = 0       #the initial sum, before any addition takes place
    while (y > 0):       #as long as y is greater than 0
        total += y % 10      #adds the last digit to the total
        y = y // 10    #removes the last digit
    return total    #returns the sum

#Requests a number from the user
num=int(input("Enter a number: "))

#calls the function as it prints the final sum
print(f"The sum of the digits of {num} is {sum_digits(num)}.")