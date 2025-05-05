#Set - UNORDERED COLLECTION WHICH IS UNORDERED , UNINDEXED 
# NO DUPLICATE VALUES 

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup","knife"}   # second set

print("Differences are ", dishes.difference(utensils))
print("Differences are ", utensils.difference(dishes)) #prints the difference in the set 
#utensils.add("napkin") # adding a element to set 
#utensils.remove("knife") #helps to remove 
#utensils.clear() # all the elements from utensils set are gone 

dishes.update(utensils)
utensils.update(dishes)  #using update function and adding 2 sets in one 
for x in utensils:
    print("Utensils are listed as ",x)

dinner_table = utensils.union(dishes)  #union function 

for x in dinner_table:
    print("Dinner table consists of ", x)          


print("Common things between both sets are ", utensils.intersection(dishes))
