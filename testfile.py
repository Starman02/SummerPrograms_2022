dictionary = {}
with open("lang.txt") as file:
 for line in file:
 
    (key, value) = line.split()
 
    dictionary[int(key)] = value

print (d)