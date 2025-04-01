# IF STATMENTS = BLOCK OF CODE THAT WILL EXECUTE IF ITS CONDITION IS TRUE 

age = int(input("how are you ? and how old : ? "))

if age == 100:
    print(" you are a centrury old")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("you arent born yet")
else:
    print("you are not an adult")
