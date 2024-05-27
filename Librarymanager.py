#Initialize empty lists, sets, and dictionary
books_list = []
authors_set = set()
books_dict = {}

#Add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"]= "John Smith"

books_list.append("Data Structure and algorithms")
authors_set.add("Jane Doe")
books_dict["Data Structure and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#Search for a book
search_title= input("Enter the title of the book")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found!")    


#Display all books
    print("List of Books:")
for book in books_list:
    print(book)

#Remove a book
remove_title = input("Enter the title of the book remove or else enter to skip:")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_title)
    del books_dict[remove_title]
    print("Books removed successfully")
    print("Books are available:",books_list)

else:
    print("Book not found!")    








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
    





    

 










