person = {} #curly brackets means it is empty and has no elements
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"} #dictionary can contain another dictionary
#to acces elements in a list you need an index value
print(person)
#add something in a list you use append. keys can't be updated. either have to delete a key or update a value
print(person['children'])#you can use type function so it can tell if you have a list or a  dictionary

print(type(person['children']))

print(person['children'][1]) #python automatically knows it's a list so you need index value (1)
#dealing with dictionary you have to give it a key
print(person['pets']['cat'])

#for i in person['children']: #person['children'] is a list # i = ralph  and every value throught he list
    #print(i) 
for i in person['pets']:
    #print(i) #i represents the key
    print(person['pets'],[i])

#for i in person ['pets'].values():
    #print(i)


