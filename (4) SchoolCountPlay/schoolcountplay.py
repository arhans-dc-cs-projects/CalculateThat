# Challenge 1 - Class List

students = int(input("How many students are in your class?"))
x = 1
namelist = []
for i in range(students):
    print("What is the name of the student number",str(x)+"?")
    studentname = input()
    namelist.append(studentname)
    studentname = None
    x = x + 1
print(namelist)
