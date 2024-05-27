
#Excercise
print("Class Excercise")

#Initialize empty lists and dictionary
students_list = []
students_dict = {}

#Ask the user to input their name,age and grade
name=str(input("enter your name:"))
age=int(input("enter your age:"))
grade=int(input("enter your grade:"))

print("student information added successfully!")

# Add student information to lists and dictionary
students_list.append("John")
students_dict["John"] = {'age': age, 'grade': grade}
print(students_dict.items())


print("Student details:")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    
#search for student's name
search_name = input("Enter student name that you want to search or simply enter to skip: ")
if search_name in students_list:
    info=students_dict[search_name]
    print(f"name:{search_name}, age:{info['age']}, grade:{info['grade']}")
else:
    print("student not found!")    

#Remove the student's name
remove_name= input("enter the name that you want to remove:") 
if remove_name in students_list:
    del students_dict[remove_name]
    students_list.remove(remove_name)
    print("student removed successfully!")
else:
    print("student not found!")



# Solution 2
book_list = ["1986", "To Kill a guy", "The End of the World"]
author_set = ["Luis Lowry", "Homer", "Mark"]
books_dict = {1: {"title": "1986" , "author" : "Luis Lowry"}, 2: {"title": "To Kill a guy", "author": "Homer"}, 3: {"title": "The End of the World", "author": "Mark"}}

search_title = input("Enter Title:")
if search_title in book_list :
    print(f"Book Avialable! Author:{books_dict[book_list.index(search_title)+1]['author']}")
else: 
    print("Book Not Avilable")

print("All Books:")
for book in book_list:
    print(book)    

remove_book = input("Enter the title of the book to be removed or skip:")
if remove_book in book_list:
    remove_author = books_dict[book_list.index(remove_book)+1]['author']
    book_list.remove(remove_book)
    author_set.remove(remove_author) 
    del books_dict[book_list.index(remove_book)+1]
    print("Book removed successfully")
    print("Books available:", book_list) 

else: 
   print("book not found")