from queue import LifoQueue
backward_history=LifoQueue()
forward_history=LifoQueue
current_page = None

#visit function
NoOfVisits=int(input("Enter the number of url history:"))
print("Enter URLs to visit:")
for i in range(NoOfVisits):
    url=input("URL:")
    print(f"Visiting{url}")
    backward_history.put(current_page)
    current_page=url
 
#Display current page
    print(f"Current page:{current_page}")

 #Go back
while input("Do you want to go back?(yes/no:)").lower()=='yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")

#Go forward
while input("Do you want to go forward?(yes/no:)").lower()=='yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No previous page available")





#Exercise

from queue import Queue

def register_patient(queue):
    name = input("Enter patient name: ")
    queue.put(name)
    print("Patient", name, "registered.")

def remove_patient(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        name = queue.get()
        print("Patient", name, "removed after meeting the doctor.")

def display_queue(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        print("Current patient queue:")
        for index, name in enumerate(queue.queue):
            print(index + 1, "-", name)

def main():
    patient_queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient(patient_queue)
        elif choice == "2":
            remove_patient(patient_queue)
        elif choice == "3":
            display_queue(patient_queue)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

                    


