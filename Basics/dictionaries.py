#Dictionaries
my_dict = {'name':'Ryan Meany', 'year':2022, 'is_male':True}
my_dict['name'] #Ryan Meany
len(my_dict) #3
list(my_dict.keys()) # ['name','year','is_male']
list(my_dict.values()) # ['Ryan Meany',2022,True]
list(my_dict.items()) # [('name':'Ryan Meany'), ('year':2022), ('is_male':True)]
my_dict.get('name') #Ryan Meany, returns none if key doesn't exist

#Add/Update item
my_dict['likes'] = 'football' # {'name':'Ryan Meany', 'year':2022, 'is_male':True, 'likes':'football'}
my_dict.update({'cool':True}) # {'name':'Ryan Meany', 'year':2022, 'is_male':True, 'likes':'football', 'cool':True}

#Remove item
del my_dict['likes']
# new_dict = my_dict.pop('likes')

#Create dictionary from a list
fruits = ["Apple","Pear","Banana"]
fruit_dictionary = dict.fromkeys(fruits, "sold") # {'Apple':'sold', 'Pear':'sold', 'Banana':'sold'}

fruits = ["Apple","Pear","Banana"]
fruit_dictionary = {fruit:"sold" for fruit in fruits } # {'Apple':'sold', 'Pear':'sold', 'Banana':'sold'}

#Merge two dictionaries with different keys
dict1 = {'a':10, 'b':8}
dict2 = {'c':6, 'd':4}
dict1.update(dict2) # Adds dict2 to dict1 {'a':10, 'b':8, 'c':6, 'd':4}
