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