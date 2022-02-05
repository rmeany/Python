#String manipulation
print(type("Hello")) #str
print("Hello"[3]) #l
me = 'Ryan Meany'
print(me[0]) #R
print(me[:]) #Ryan Meany
print(me[1:]) #yan Meany
print(me[:1]) #R
print(me[-1]) #y
print(me[::-1]) #ynaeM nayR
print(len(me)) #10
print(me.strip()) #Strips whitespace
print(me.replace('Ryan','BetterRyan')) #BetterRyan Meany
print(me.replace('y','')) #Ran Mean
print(me.startswith('Ryan')) #True
print(me.index('n')) #3
print(me.upper()) #RYAN MEANY
print(me.lower()) #ryan meany
print(me.find('a')) #First position of 'a' -> 2
print(me.count('a')) #Count how many instances of 'a' -> 2

#String formatting
print(f'Hello, my name is {me}')
print('Hello, my first name is {} and surname is {}'.format(me.split(' ')[0], me.split(' ')[1]))
print('Hello, my name is %s and the year is %d' %(me, 2022))

#String palindrome check
word = 'reviver'
#Method1
is_palindrome = False
if (word == word[::-1]):
    is_palindrome = True
print(is_palindrome)

#Method2
is_palindrome = bool(word.find(word[::-1])+1)
print(is_palindrome)
