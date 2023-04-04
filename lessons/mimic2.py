"""Practice Writing Functions"""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return ("Too high of an index.") 
   #If we made it here, that means the letter_idx is valid. Return is the last line and fuction exits.
    else:
        return my_words[letter_idx]

mimic_letter("hello!",0)
print(mimic_letter("hello!",0))