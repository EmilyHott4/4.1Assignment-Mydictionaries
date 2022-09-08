import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook)) #type is a function in python that allows us to know what type of function you are dealing with (list or dictionary)
# a key error means that value is not in your dictionary
phone = phonebook['Chris']

print(phone)

print(len(phonebook)) #know the length of dictionary

#mydictionary = dict(m=8, n=9) #another way to creat a dictionary through 'dict' function and give them a key value pair
#m and n are string
#8 and 9 are numbers
mydict = {} #creates an empty dictionary
print(mydict)


#print(mydictionary)



print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********') #search a dictionary
print()

name = 'Chris'

if name in phonebook:
    print(phonebook[name])  #you give the key, it gives back the value
else:
    print (name, 'not found')







print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123' #updates the dictionary with new number for chris
phonebook['Joe'] = '555 - 4444' #adds Joe to the dictionary with a key valued pair
print(phonebook)




print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris'] #deletes chris from dictionary
#if the key does not exist in dictionary you will get an error
#print(phonebook)



print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

#use for loop to iterate one by one
for k in phonebook: #'k' used to be 'key'
    print(k) #prints the names of the phonebook #iterates through the keys, its the default option
    print(phonebook[k]) #key is just a variable you named, can change it to anything like 'k'

for value in phonebook.values():#.values allows you to cycle through the values
    print(value)
    
#for k,v in phonebook.items():
    #print('key:', k 'value: ' , v)

for tuple in phonebook.items(): #immutable = can't change mutable means you can change them
    print(tuple)






print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("Chris,","key not found")
print(phone)

#phonebook.clear()
#print(phonebook)






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#remove = phonebook.pop('Chris','key not found')

#print(remove)
#print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#picks random key value pair
#a = phonebook.popitem() #don't need to give it key cause picks an element
#always picks the last element

#print(a)
#print(phonebook)





print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys) #when you use a list on dictionary it creates a list with just the keys

random_key = random.choice(list_of_keys)
print(random_key)

print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])
#exactly the same thing as above



print()
print('*****  end section 9 ********')
print()

#random.choice will pick random element from list





