#Lists Functions 

#list  - Used to store multiple items in a single variable


food = ["Pizza","Burgers","Frenchfries","chillicheese","Smilies"]
print(food[4])

food[0] = "Panner"
#Append function
food.append("ice cream")
#REMOVE FUNction 
food.remove("Smilies") 
#POP FUNCTION 
food.pop() # removes an item

#add or change 
food.insert(0,"cake") # added cake instead of PIzza now
food.sort()
#food.clear() # clears the list completely 
print(food[0]) # changed oth item to panner from pizza

#to print all the contents in the list lets add for loop

for x in food:
    print("The list of food is here ", x)




