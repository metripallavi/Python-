#Tuple - COLLECTION WHICH IS ORDERED AND UNCHANGEABLE USED TO GROUP TOGETHERT REALTEAD DATA

student = ("Ram",21,"male")

print(student.count("Ram"))  #count tuple function 
print(student.index("male"))  # function index in tuple 


for x in student:
    print(x)

if "Ram" in student:
    print("Ram ist here !")

