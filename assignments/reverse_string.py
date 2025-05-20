# A python program that reverses a string entered by a user

#define the function that will reverse the string
def reverse_string(str1):
    str2 = ''    #this is an empty string, str2 that will store the reversed string
    length = len(str1)     #find the length of the original string

    #the for loop goes through each character, from the first to the last
    for i in range(-1, -length - 1, -1):
        str2 += str1[i]    #adds each character from str1 (as it does the reversing) to str2
    return str2    #returns the final string that has been reversed

#request the user to type in a string
str1 = input("Enter a string or sentence: ")
str2 = reverse_string(str1)    #we call the function that will reverse the string from the user, str1

#print the original and reversed string
print(f"\nThe original string is: {str1}")
print(f"The reversed string is: {str2}")