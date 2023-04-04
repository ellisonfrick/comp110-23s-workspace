"""Short words"""

def short_words(list_1: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 character"""
    empty = []
    for idx in list_1:
        if len(idx) < 5:
            empty.append(idx)
        else: 
            print(f"{idx} is too long")
    return empty

my_list : list [ str ] = [ "sun", "cloud", "sky" ]
short_words( my_list )