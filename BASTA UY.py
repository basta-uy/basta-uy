FILENAME = "students.txt"

# Create file if it doesn't exist
try:
    file = open(FILENAME, "x")
    file.close()
except FileExistsError:
    pass