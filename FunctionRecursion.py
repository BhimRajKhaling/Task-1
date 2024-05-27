def sum_of_digits(n):
    if n<10:
        return n
    else:
        last_digit=n%10
        remaining_digits=n//10

        return last_digit+sum_of_digits(remaining_digits)
    
print(sum_of_digits(123))  


# Guide: Function to calculate the sum of digits using recursion
def sum_of_digits(n):
    # Base case: if n is a single-digit number, return n
    if n < 10:
        return n
    else:
        # Extract the last digit
        last_digit = n % 10
        # Remove the last digit from n
        remaining_digits = n // 10
        # Recursive call to sum_of_digits with the remaining digits
        return last_digit + sum_of_digits(remaining_digits)

# Test the function
print(sum_of_digits(17863)) 

###EXERCISE PART 
# Recursive function to reverse a string
def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it as it is
    if len(s) <= 1:
        return s
    else:
        # Recursive case: reverse the substring excluding the first character
        # and then append the first character to the end
        return reverse_string(s[1:]) + s[0]

# Test cases
input_strings = ["hello", "python", ""]
for s in input_strings:
    print(f"Input: {s}, Output: {reverse_string(s)}")




#Exercise of function Recursion

def reverse_string(s):
    # Base case: if the string is empty or contains only one character,
    # return the string as it is
    if len(s) <= 1:
        return s
    else:
        # Recursive case:
        # Separate the first character from the rest of the string
        first_char = s[0]
        rest_of_string = s[1:]
        # Recursively call reverse_string on the rest of the string
        reversed_rest = reverse_string(rest_of_string)
        # Append the first character to the reversed string
        reversed_string = reversed_rest + first_char
        return reversed_string

# Examples
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python")) # Output: "nohtyp"
print(reverse_string(""))       # Output: ""
