"""Practice Writing Functions"""

def mimic(my_words: str) -> str:
    """Given the strong my_words, outputs the same string"""
    return my_words

mimic("Hello!")  #one way to call

print(mimic("Hello!"))

my_words: str = "Hello!"  #Another way to call
response: str = mimic(my_words)
print(response)