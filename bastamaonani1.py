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