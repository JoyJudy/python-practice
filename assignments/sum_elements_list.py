#defining the function called 'sum_elements', takes one parameter 'numbers'
#'total' stores the output, and starts at 0, since no addition has been done

def sum_elements(numbers):
    total = 0

    #for loop will go through the list of numbers in the list
    #i is the current number from the list
    for i in numbers:
        #add the current number to the running total
        total = total + i
    #after going through all the numbers in the list, return the final total
    return total

#creating a list of numbers in an array
my_list = [1,2,3,4,5]
my_list2 = [4,35,35,56,675]

#call the function with the test list and store the result
result = sum_elements(my_list)
result2 = sum_elements(my_list2)

#print solution
print(f"The sum of {my_list} is {result}")
print(f"The sum of {my_list2} is {result2}")

