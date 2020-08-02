vow = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word for the program to look for: ")
found = []
for letter in word:
    if letter in vow:
        if letter not in found:
            found.append(letter)

print(found)
