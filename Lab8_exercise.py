def find_first_repeating_character(s):
   
    char_count = {}
    
    for char in s:
        if char in char_count:
           
            print(f"First repeating character: {char}")
            print(f"Memory address: {id(char)}")
            return char, id(char)
        else:
         
            char_count[char] = 1
    
  
    return None


result = find_first_repeating_character("swiss")
if result:
    char, address = result
    print(f"The first repeating character is '{char}' with memory address {address}.")
else:
    print("No repeating character found.")




#Solution2
# Exercise
def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it's already there, print the character and its memory address
            print(f"First repeating character: {char}, Memory address: {id(char)}")
            return char, id(char)
        else:
            # If not, add it to the dictionary with a count of 1
            char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Example usage:
string = "abcdefgabc"
result = find_first_repeating_character(string)
if result is None:
    print("No repeating character found.")    