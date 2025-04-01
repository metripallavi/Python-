#NESTED LOOPS = THE INNER LOOP WILL FINISH ALL OF ITS ITERATIONS BEFORE #
# FINISHING ONE ITERATION OF THE "OUTER LOOP"

rows = int(input("Enter the no of rows :" ))
columns = int(input("Enter the no of col :"))
symbol = input("Enter the symbol you want : ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

