n = int(input("Enter the number for which you want the multiplication table: "))
m = int(input("Enter the limit for the table: "))
i = 1

while i <= m:
    i += 1
    print(f"{n} * {i} = {n * i}")
for i in range(1,9):
    if i == 3:
        continue

    if i == 7:
        break
    print(i)

h = int(input("Enter the height for the triangle: "))
for row in range(h):
    for star in range(row+1):
        print("*", end='')
    print()