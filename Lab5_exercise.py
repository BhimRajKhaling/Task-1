from queue import Queue

# Initializing a queue to store patient names
patient_queue = Queue()

# Function to register a new patient
def register_patient():
    name = input("Enter patient name: ")
    patient_queue.put(name)
    print(f"Patient {name} registered.")

# Function to remove the next patient after meeting the doctor
def remove_patient():
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        removed_patient = patient_queue.get()
        print(f"Patient {removed_patient} removed after meeting the doctor.")

# Function to display the current patient queue
def display_patient_queue():
    if patient_queue.empty():
        print("No patients in the queue.")
    else:
        print("Current Patient Queue:")
        while not patient_queue.empty():
            print(patient_queue.get())
        patient_queue.queue.clear()

# Main menu function
def main_menu():
    while True:
        print("\nDesk Manager Patient Registration and Appointment System")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice (just enter the option number): ")

        if choice == '1':
            register_patient()
        elif choice == '2':
            remove_patient()
        elif choice == '3':
            display_patient_queue()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the main menu function
if __name__ == "__main__":
    main_menu()