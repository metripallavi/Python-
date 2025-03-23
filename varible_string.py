#Knowing Datatypes 
#String #Int #Float #Boolean 

First_name = "Pallavi"
Last_name = "Metri"
Full_name = (First_name + " " + Last_name)
print(Full_name)

age = 27   #Int datatype 
age += 1
print (age) 
print ("My age is:"+ (str(age))) #String concatnation

Height = 174.2 #Float Datatype
print(Height)
print (" my height is : " + str(Height) + "cm" ) 
print (type(Height))

#Boolean Datatype 
human = True
print(human)
print("Are you a Human : ? "+ (str("yes")))
print(type(human))

#Multiple Assignent

name = "PC"
age = 28
beautiful = True 

#print(name)
#print(age)
#print(beautiful)

#so instead of printing like above we can print them in same line to save time and line of code 
print(name,age,beautiful)
