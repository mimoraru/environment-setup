vow = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word for the program to look for: ")

found = {}

for letter in word:
    if letter in vow:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
