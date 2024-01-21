from collections.abc import Callable
from unicodedata import normalize

import re

def sylabize(text: str, max_letters: int = 4, 
            unknow_manager:str|Callable[[str], any] = None, 
            strip_spaces: bool = True, strip_nonletters: bool = True,
            strip_others: re.Pattern = None
        ) -> list:
    """
    Sylabize a text.
    Sylabizing means spliting a text in groups of letters with a specific pattern / following a specific ruling.
    Inputs:
        text: str
            The text to sylabize.
        max_letters: int
            The maximum number of letters in a sylable. Default to 4 which is a common maximum. Can be None for no limit.
        unknow_manager: str|Callable[[str], Any]
            The way to handle unknow sylables. Unknown sylables would appear when there is no appearent rule for the sylabization process.
            Can be a string or a function or None.
            If a string, it will replace the unkwon sylable.
            If a function, it will be called with the unknow sylable as argument and its value will replace the unkwnon sylable.
            If None, the unknow sylable will be kept as is.
    Returns:
        A list of sylables. Each sylable is a string unless the unknow_manager is a function, in which case it can be anything.
    """

    syllables = []
    i = 0 # index of the first letter of the current sylable
    j = 0 # index of the last letter of the current sylable
    while i < len(text):
        while j <= len(text):
            j += 1
            sylable_to_test = preprocess_sylable(text[i:j], strip_spaces, strip_nonletters, strip_others)
            if test_sylable(sylable_to_test, text[j]): # test_sylable to test if the current sylable is valid
                syllables.append(sylable_to_test)
                i = j
                break
            elif (max_letters is not None and j - i >= max_letters) or j == len(text): # if it is not a valid sylable and we reached the max number of letters or the end of the text use the unknow_manager
                if unknow_manager is None:
                    syllables.append(sylable_to_test)
                elif isinstance(unknow_manager, str):
                    syllables.append(unknow_manager)
                else:
                    syllables.append(unknow_manager(sylable_to_test))
                i = j
                break
            print(i, j, syllables)
    
    return syllables

def test_sylable(sylable: str, next_letter: str) -> bool:
    """
    Test if a sylable is valid. It uses not only the current sylable but also the following letter to determine if the sylable is valid.
    Inputs:
        sylable: str
            The sylable to test.
        next_letter: str
            The next letter of the text after the sylable.
    Returns:
        True if the sylable is valid, False otherwise.
    """
    
    print('testing', sylable, next_letter)
    # If next letter is not a word character, the sylable is valid
    # since next_letter could have accents it must be normalized before tested with \W
    if re.search(r'\W', normalize('NFKD', next_letter)):
        return True
    
    return False

def preprocess_sylable(text, strip_spaces: bool, strip_nonletters: bool, strip_others: re.Pattern):
    if strip_spaces:
        text = text.strip()
    if strip_nonletters:
        # since the text could have accents it must be normalized before running the strip
        pass
    if strip_others is not None:
        text = strip_others.sub(strip_others, text)
    return text