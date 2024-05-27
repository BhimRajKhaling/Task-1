

# Example 1# AND Operator (both conditions need to be true to get output as true)
x= 5
print(x > 3 and x < 10)

#Example 2
y= 12
print(y>10 and y % 5 == 0)

#OR Operator( )
#example 1 
x=5
print(x<3 or x> 10)

#example 2
y=12
print(y<10 or y % 2 ==0)


#NOT Operator
#example 1
x= 5
print(not(x>3 and x < 10 ))

#example 2
y=12 
print(not(y>10 and y % 5== 0))



# Excercise

age = int(input("Enter your age: "))
is_student = input("Are you a student (yes/no): ") .lower()

# Check eligibility for discount
if age <= 12 or (13<=age <=18 and is_student == 'yes'):
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")





