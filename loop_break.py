
# LOOP CONTROL STATEMNTS = CHANGE A LOOP EXECTION FROM ITS NORMAL SEQUENCE 

# break = used to termiante the loop entierly
# continue = skips to next iteration in the loop
# pass = does nothing , acts as a placeholder 

#break loop 
while True:
    name = input("enter your name: ")
    if name != "":
        break

#continue loops

phone_no = "123-456-847"

for i in phone_no:
     if i == "-":
         continue
     print(i,end="")

#pass loop 
for i in range(1,21):

    if i == 13:  # i dont want to prin this number 
        pass
    else:
        print("so i is ", +i)  # check output 13 is not printed lol 


