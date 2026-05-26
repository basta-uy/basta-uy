FILENAME = "students.py"

try:
    with open(FILENAME, "x"):
        print("Student file created!")
except FileExistsError:
    print("Student file already exists!")

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    with open(FILENAME, "a") as file:
        file.write(f"{student_id},{name},{course}\n")

    print("Student added successfully!")

def view_students():
    try:
        with open(FILENAME, "r") as file:
            students = file.readlines()

            if len(students) == 0:
                print("No student records found.")
            else:
                print("\n--- Student Records ---")

                for student in students:
                    student_id, name, course = student.strip().split(",")

                    print("ID:", student_id)
                    print("Name:", name)
                    print("Course:", course)
                    print("------------------")

    except FileNotFoundError:
        print("File not found.") 

def search_student():
‎    search_id = input("Enter Student ID to search: ")
‎
‎    with open(FILENAME, "r") as file:
‎        found = False
‎
‎        for student in file:
‎            student_id, name, course = student.strip().split(",")
‎
‎            if student_id == search_id:
‎                print("\nStudent Found")
‎                print("ID:", student_id)
‎                print("Name:", name)
‎                print("Course:", course)
‎                found = True
‎
‎        if not found:
‎            print("Student not found.")
‎
‎
‎def delete_student():
‎    delete_id = input("Enter Student ID to delete: ")
‎
‎    with open(FILENAME, "r") as file:
‎        students = file.readlines()
‎
‎    with open(FILENAME, "w") as file:
‎        found = False
‎
‎        for student in students:
‎            student_id, name, course = student.strip().split(",")
‎
‎            if student_id != delete_id:
‎                file.write(student)
‎            else:
‎                found = True
‎
‎    if found:
‎        print("Student deleted successfully!")
‎    else:
‎        print("Student not found.")
‎
‎
‎while True:
‎    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
‎    print("1. Add Student")
‎    print("2. View Students")
‎    print("3. Search Student")
‎    print("4. Delete Student")
‎    print("5. Exit")
‎
‎    choice = input("Enter choice: ")
‎
‎    if choice == "1":
‎        add_student()
‎
‎    elif choice == "2":
‎        view_students()
‎
‎    elif choice == "3":
‎        search_student()
‎
‎    elif choice == "4":
‎        delete_student()
‎
‎    elif choice == "5":
‎        print("Program Closed")
‎        break
‎
‎    else:
‎        print("Invalid choice.")