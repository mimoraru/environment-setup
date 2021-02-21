def search_for_word(word: str) -> set:
    """This funtion will return the vowels found in a word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_for_phrase(phrase: str, letters: str) -> set:
    """This funtion will return the letters found in a specified phrase"""
    return set(letters).intersection(set(phrase))


print(search_for_phrase('lulu are mere', 'uat'))
