 
# Excercise

age = int(input("Enter your age: "))
is_student = input("Are you a student (yes/no): ") .lower()

# Check eligibility for discount
if age <= 12 or (13<=age <=18 and is_student == 'yes'):
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
