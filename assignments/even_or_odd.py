#defining the function that checks whether a number x is odd or even
def check_even_odd(x):
    if x % 2 == 0: #is the number even
        print(f"The number {x} is even.")     #if it is even, return true
    else:
        print(f"The number {x} is odd.")   #if it is not even i.e. odd, return false

#Request input from the user
n= int(input("Enter number: ")) #turns the string into an integer

#calling the function check_num, and passing it to n
check_even_odd(n)