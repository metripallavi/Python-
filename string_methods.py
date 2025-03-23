name = "pallavi"

print(name)
print(len(name)) # PRINTS length of the string
print(name.find("v")) #using find to find letters first occurance only 
print(name.capitalize()) # helps in captitalize my first letter
print(name.upper()) #Makes entire name capital 

name1 = "METRI"
print(name.lower()) #prints all the letters in lower
print(name.isdigit(),name1.isdigit())  # helps in identifiying if its digit or not

print(name.isalpha(),name1.isalpha()) #helps in identifying if the string is conatains alphabetic letters or not

print(name.count("a") , name1.count("I")) # helps in identifying letters repetations

print(name.replace("a" , "x") , name1.replace("M" , "P")) # replacing letters 

print(name*4)
