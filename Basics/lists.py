#Lists
my_list = [1,2,'3',True]
print(len(my_list)) #4
my_list.append(100) # [1,2,'3',True,100]
my_list.extend([101,102]) # [1,2,'3',True,100,101,102]
my_list.insert(2, '?') # [1,2,'?','3',True,100,101,102]

#Copy Lists
new_list = my_list.copy()
new_list_2 = my_list[:]

#Remove From List
my_list.pop() #Removes last index from list (default is -1) -> [1,2,'?','3',True,100,101]
my_list.pop(2) #Removes item at index 2 from list -> [1,2,'3',True,100,101]
my_list.remove(100) #Removes first occurence from list or else raises ValueError -> [1,2,'3',True,101]
my_list.clear() #Removes all items from list -> []

#Order List
my_list = [1,9,3,7]
my_list.sort() #Orders list by lowest->highest [1,3,7,9]
my_list.sort(reverse=True) #Orders list by highest->lowest [9,7,3,1]
my_list.reverse() #Reverses list [7,3,9,1]
print(sorted(my_list)) # [1,3,7,9]
print(list(reversed([1,9,3,7]))) #Reverses list [7,3,9,1]

#Handy Operations
my_list = [1,2,30,4,5]
print(2 in my_list) #True
print(min(my_list)) #1
print(max(my_list)) #30
print(sum(my_list)) #42

#List Comprehensions
[char for char in 'Hello'] #New List -> ['H','e','l','l','o']
list_of_chars = list('Hello') # ['H','e','l','l','o']
[i*2 for i in [1,2,3]] #New List -> [2,4,6]
[i for i in range(0,10) if i % 2 == 0] #New List -> [0,2,4,6,8]
