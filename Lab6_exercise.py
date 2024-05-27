# Exercise 1

n = int(input("Enter the number for which you want the multiplication table: "))
m = int(input("Enter the limit for the table: "))
i = 1

while i <= m:
    i += 1
    print(f"{n} * {i} = {n * i}")



# Exercise 2
h = int(input("Enter the height for the triangle: "))
for row in range(h):
    for star in range(row+1):
        print("*", end='')
    print()




# Exercise 3
for i in range(1, 10):
    # Skip printing number 3 in the inner loop
    if i == 3:
        continue
    
    # Break out of the outer loop when reaching number 7
    if i == 7:
        break
    
    # Print the current number
    print(i)
