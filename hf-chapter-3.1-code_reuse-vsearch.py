
def search4vowels():
    """Display any vowels in an asked for word"""
    vow = ['a', 'e', 'i', 'o', 'u']
    word = input("Provide a word for the program to look for: ")
    found = set(vow).intersection(set(word))
    print(found)
