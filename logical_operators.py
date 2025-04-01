#LOGICAL OPERATOR'S (AND , OR , NOT ) = USED TO CHECK IF 2 OR MORE CONDITIONAL STATMENTS ARE TRUE #


temp = int(input("Hey , What's the temprature : ? "))

if temp >= 0 and temp <= 30:
    print("The temprate is great today")
    print("Go outside buddy")

elif temp < 0 or temp > 30:
    print("Temprature isnt that great,\n"  "Stay indoors !! ")

elif not(temp >= 0 and temp <= 30):   #flips true to false and flase to true 
    print("The temprate is great today")
    print("Go outside buddy")

