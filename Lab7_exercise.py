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