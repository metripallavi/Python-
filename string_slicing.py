#slicing = create a substring by extracting elements from another string 
#indexing [] or slice ()
# [start:stop:step]

name = "Pallavi Metri"

first_name = name[:3]  #[0:3]
print(first_name)

last_name = name[4:8]  #[4:end]
print(last_name)

funny_name = name[0:8:2] #[0:end:2]
funny_name = name[::3]
print(funny_name)

#Resverse string 
reversed_name = name[::-1] # [0:end:-1]
print(reversed_name)


#Slicing 

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])

print(website2[slice])


