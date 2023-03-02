"""EX03 - Structured Wordle!"""

__author__ = "730566890"

def contains_char(word: str, char: str) -> bool:  # function that searches for a character in the word
    """Function searches for character within word"""
    assert len(char) == 1
    i: int = 0

    while i < len(word):  # While loop to check for character
        if word[i] == char:
            return True
        else:
            i = i + 1
    return False

WHITE_BOX: str = "\U00002B1C"  # White emoji box if letter not found
GREEN_BOX: str = "\U0001F7E9"  # Green emoji box if letter found and in correct place
YELLOW_BOX: str = "\U0001F7E8"  # Yellow emoji box if letter found in the wrong place

def emojified(guess: str, secret: str) -> str:  # Function that determines which emoji is going to be used
    """If index matches in guess and secret will print green box. If guess is in secret but wrong place, will print yellow box. If guess is not in secret, white box"""
    assert len(guess) == len(secret)
    idx: int = 0
    response: str = ""

    while idx < len(guess):  # While loop to assign emoji with each letter in guess based on secret
        if guess[idx] == secret[idx]:
            response = response + GREEN_BOX
        elif contains_char(secret, guess[idx]) is True:
            response = response + YELLOW_BOX
        else:
            response = response + WHITE_BOX
        idx = idx + 1
    return response

def input_guess(character: int) -> str:  # Function that makes sure length of guess is correct
    """Prompt user for a guess until they guess expected length and then return guess"""
    guess: str = input(f"Enter a {character} character word: ")

    while len(guess) != character:
        guess = input(f"That wasn't {character} chars! Try again: ")
   
    if len(guess) == character:
        return guess

def main() -> None:  
    """The entrypoint of the program and main game loop"""
    turn: int = 1
    word: str = "codes"
    playing: bool = True

    while turn <= 6 and playing is not False:  # Makes sure turn is only 6
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(word))
        print(emojified(guess, word))
        if guess == word:
            playing = False
        else:
            turn = turn + 1

    if playing is False:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":  # Calling for the functions
    main()