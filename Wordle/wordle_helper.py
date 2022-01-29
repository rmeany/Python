import sys

# Read in possible words
dictionary = open("words.txt", "r")
words = dictionary.read().splitlines()
dictionary.close()

solutions = []

# remove new lines from words in array, put them into solutions array
for word in words:
   solutions.append(word)

# Keep words that contain letters we know exist
solutions = [word for word in solutions if all(char in word for char in sys.argv[1])]

# Keep words that don't contain letters we know don't exist
solutions = [word for word in solutions if all(char not in word for char in sys.argv[2])]

for word in solutions:
    print(word)
