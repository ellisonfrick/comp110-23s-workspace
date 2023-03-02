"""EX02 - One shot wordle!"""

__author__ = "730566890"
Secret: str = "python"
Length: int = len(Secret)
Guess: str = input(f"What is your {Length}-letter guess?")


while len(Guess) != len(Secret):  # When guess doesn't equal length of secret
    Guess = input(f"That was not {Length} letters! Try again:")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
resulting_emoji: str = ""

while index < len(Secret):  # Character in guess matches character in secret word
    playing: bool = False
    alt_index: int = 0

    if Guess[index] == Secret[index]:  # Green box added for correctly guessed character in correct spot
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        while playing is not True and alt_index < len(Secret):
            if Guess[index] == Secret[alt_index]:
                playing = True
            alt_index = alt_index + 1
        if playing is True:  # Yellow box added for correctly guessed character in wrong spot
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:  # White box added for incorrectly guessed character
            resulting_emoji = resulting_emoji + WHITE_BOX
    index = index + 1  # Check next character      
print(resulting_emoji)  # Emojis printed

if Guess == Secret:  # When guess is correct
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
