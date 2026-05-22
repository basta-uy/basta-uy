FILENAME = "students.txt"

try:
    file = open(FILENAME, "x")
    file.close()
except FileExistsError:
    pass
