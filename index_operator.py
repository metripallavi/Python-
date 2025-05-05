# INDEX OPERATOR IN PYTHON - GIVES ACCESS TO SEQUENCE'S ELEMENTS (STR ,LIST,TUPLES)


name = "pallavi metri!"

if(name[0].islower()):
    name = name.capitalize()

print("Capitalized name is ", name)

first_name = name[0:3].upper()
print(first_name) # uppercase function only from 0 to 3 rd lettter of name in first name
last_name = name[4:].lower() 
print(last_name) # lowercase function and  only from  lettter of name in last name 
last_character = name[-1] #using negative indexing should print ! mark , if used -2 it will print i
print(last_character)

