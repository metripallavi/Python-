#DICTIONARY - CHANGABLE, UNORDERED COLLECTION OF UNIQUE KEY : VALUE PAIRS
#FAST - BECAUSE THEY USE HASING , ALLOWS US TO ACCESS A VALUE QUICKLY

capitals = {'USA' : 'Washington DC',
            'INDIA' : 'New Delhi',
            'CHINA' : 'Beijing',
            'RUSSIA' : 'Moscow'}

capitals.update({'GERMANY':'BERLIN'})
capitals.update({'USA' : 'LA'})  # updates usa capital to LA
#capitals.pop('CHINA') #helps to remove keyvalue pair from the dictonary
capitals.clear() # clears everything from dictonary 
#print(capitals["RUSSIA"])
#print(capitals["Germany"])
#print(capitals.get('Germany')) #get method helps to find if germany exists or not 

print("Dictionary consists of", capitals.keys())  #prints all the keys from dictionary 
print(capitals.values()) # print the values of the dictonary 
print("The dictionary has", capitals.items()) #prints everything

for key,value in capitals.items() :
    print("Keys and the values are", key ,value)

