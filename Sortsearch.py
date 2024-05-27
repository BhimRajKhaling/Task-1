def bubble_sort_2d(arr):
    n=len(arr)   # Number of rows in the 2D array
    m=len(arr[0])  # Number of columns in the 2D array; assumes all rows have equal length
    total_elements = n*m  # Total number of elements in the 2D array

    for i in range(total_elements - 1):
        # Outer loop: goes through all elements in the 2D array

        for j in range(total_elements-1-i):
            #Inner loop: goes through the elements, reducing the comparison range each time

            # Calculate current position in 2D terms
            row1=j//m
            col1=j%m

            # Calculate next position(right next to current position)
            row2=(j+1)//m
            col2=(j+1)%m

            #Compare and possibly sawp elements
            if arr[row1][col1] > arr[row2][col2]:
                # If the current elements is greater than the next, swap them
                arr[row1][col1], arr[row2][col2] = arr[row2][col2],arr[row1][col1]

def search_element(arr, element):
    found= False    # Initialization a flag to track if the element is found
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                print(f"Element found at position: row = {i}, column={j}")
                found= True
                return    # Exit the function after finding the element
    if not found:
        print("Element not found in the given array.")


# Example usage:
arr = [
    [9, 2, 3]
    [4, 5, 6]
    [7, 8, 1]
] 

print(arr)
bubble_sort_2d(arr)
print(arr)

# Searching for an element
search = int(input("Enter the element to search:"))
search_element(arr, search)






# Exercise of sorting
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement

# Prompt the user to input an array of integers
arr = [int(x) for x in input("Enter the array of integers separated by spaces: ").split()]

# Sort the array using quick sort
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# Allow the user to specify a target element to search for
target = int(input("Enter the target element to search for: "))

# If the target element is found, prompt the user to input a replacement element
if target in sorted_arr:
    replacement = int(input(f"Enter the replacement element for {target}: "))
    # Replace all occurrences of the target element with the replacement element
    replace_elements(sorted_arr, target, replacement)
    print("Modified array after replacing elements:", sorted_arr)
else:
    print("Target element not found in the array.")


