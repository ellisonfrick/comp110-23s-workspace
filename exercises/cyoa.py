"""EX06 - Choose your own adventure!"""

__author__ = "730566890"
from random import randint

player: str
points: int = 0
named_constant: str = "\U00002705"
named_constant_1: str = "\U0000274C"


def main() -> None:  # Main function
    """Goes through all functions!"""
    global player
    global points
    playing: bool = True
    greet()
    while playing is True:
        option: int = int(input("To begin, choose a number 1 to end battle, 2 to prepare for battle, or 3 to begin battle: "))
        if option == 1:
            print(f"Thank you for playing! Adventure points:{points}")
            playing: bool = False
        elif option == 2:
            prepare()
            print(f"Congrats! You are prepared with {points} amount of points! Now head to battle!")
        else:
            xs: int = battle(0)
            print(f"Thank you for playing {player}! You finished with {xs} points")
            playing: bool = False

        
def greet() -> None:  # Greet message
    """Welcome Message!"""
    global player
    player_1: str = str(input("What is your name? "))
    player = player_1
    print(f"Welcome to the Battle Game {player}!")


def prepare() -> None:  # Choosing options in order to earn points for battle
    """Choose which weapon you want!"""
    global player
    global points
    global named_constant
    global named_constant_1
    choice: int = int(input("If your name has more than five letters, you recieve two bonus points instead of one. Choose 1 or 2 for sword choice to see how many other points you can earn: "))
    if len(player) > 5:
        points += 2
    else:
        points += 1

    if choice == 1:
        print(f" {player} you recieved 1 bonus point that will help you last longer in battle!")
        points += 1
    else:
        print(f" {player} you recieved 2 bonus points that will help you last longer in battle!")
        points += 2
    choice_1: int = int(input("Now it is time to choose which armour you want! Each other comes with a differnet amount of point. Choose 1 for red. Choose 2 for blue. Choose 3 for silver. "))
    if choice_1 == 1:
        print(f"Sorry {player}, red does not come with any bonus points." + named_constant_1)
    elif choice_1 == 2: 
        print(f"Congrats {player}! You recieved 1 point for choosing blue armour." + named_constant)
        points += 1
    else: 
        print(f"Congrats {player}! You recieved 2 points for choosing blue armour." + named_constant)
        points += 2
    choice_2: int = int(input("Lastly, it is important that you choose your sidekick that also gives you points! Choose 1 to for a dog. Choose 2 for a cow. Choose 3 for a sheep. "))
    if choice_2 == 1:
        print("The dog was a great choice and gives you 6 points!")
        points += 4
    elif choice_2 == 2:
        print("The cow was a great choice and gives you 7 points!")
        points += 4
    else:
        print("The sheep was a great choice and gives you 5 points!")
        points += 3
    choice_3: int = int(input("Before heading to battle, would you like to pay 5 points and win up to 10 points? However, if you inccorectly solve the questions you do not win anything. Enter 1 for yes or 2 for no: "))
    if choice_3 == 1:
        points -= 5
        print("Yay! Your surprise purchase consist of battle trivia! You get one chance to answer")
        trivia_0: int = int(input("What year did World War II begin? 1939, 1940, or 1920?: "))
        if trivia_0 == 1939:
            print(named_constant + "Correct! You earned 2 points")
            points += 2
        else: 
            print(named_constant_1 + "Sorry, that was incorrect")
        trivia_1: int = int(input("Which modern video game has different types of armour and swords? |*ENTER #| 1-Mario Kart. 2-Minecraft. 3-Among Us: "))
        if trivia_1 == 2:
            print(named_constant + "Correct! You earned 2 points")
            points += 2
        else:
            print(named_constant_1 + "Sorry, that was incorrect")
        trivia_3: int = int(input("Silver is commonly used to make armmour. Approximately how much is a pound of silver worth (in USD)? 150, 380, 270?: "))
        if trivia_3 == 270:
            print(named_constant + "Correct! You earned 2 points")
            points += 2
        else:
            print(named_constant_1 + "Sorry, that was incorrect")
        trivia_4: int = int(input("Finally, what year was the Battleship game officially released? 1930, 1967, 1989?: "))
        if trivia_4 == 1967:
            print(named_constant + "Correct! You earned 4 points")
            points += 4
        else:
            print(named_constant_1 + "Sorry, that was incorrect")
    else: 
        print("You saved your points and are finally prepared for battle!")
    

def battle(x: int) -> int:  # Function where you make choices to fight and become stronger
    """Entering battle!"""
    global player
    global named_constant
    x: int = points
    tries: int = 0
    playing: bool = True
    print(f"You have {x} points to begin with. Losing battles takes away these points, but winning battles earns you points. Collect 15 points to win, but don't let your points reach 0 or the game is over.")
    if x > 15:
        print(named_constant + f"Congrats {player} you successfully completed the game!")
        return x
    else:
        while x > 0 and tries < 2:
            playing is True
            begin: int = int(input(f"Are you ready to begin {player}? Choose 1 to go left to enter the cave or choose 2 to go right to climb the mountain:  "))
            if begin == 1:
                cave: int = int(input("You have chosen to enter the cave. It is dark, but you have the option to buy a flashlight for 2 points. Enter 1 to buy the flashlight or 2 to continue without: "))
                if cave == 1:
                    x -= 2
                    print(f"Yay {player} you can see now! Oh no, it looks like there is a giant ahead that you need to defeat. Use your sword and sidekick to help you.")
                    win: int = randint(1, 2)
                    if win == 1:
                        print("Yay! You defeated the enemy! You earned 1 point")  
                        x += 1
                    else:
                        print("Oh no! You were defeated by the enemy. You lost 2 points")
                        x -= 2
                elif cave == 2:
                    print(f"Oh no {player}! You ran into giant because you couldn't see in the cave. You lost 2 points")
                    x -= 2
            elif begin == 2:
                mountain: int = int(input("You have chosen to climb the mountain, but the mountain ends soon. Enter 1 to buy a rope for 2 points to get across to the other side or 2 to turn around: "))
                if mountain == 1:
                    x -= 2
                    print("You have crossed to the other side! There is a dragon across from you. Use your sword and sidekick to help you battle them.")
                    win: int = randint(1, 2)
                    if win == 1:
                        print("Yay! You defeated the enemy! You earned 1 point")  
                        x += 1
                    else:
                        print("Oh no! You were defeated by the enemy. You lost 2 points")
                        x -= 2
                elif mountain == 2:
                    print("You turn around to climb back down the mountain but see a dragon. Since there is nowhere to go you are defeated. You lost 2 points")
                    x -= 2
            tries += 1
            print(f"You now have {x} points! Continue to your next adventure!")
        tries_1: int = 0
        print("Congrats on making it past the first round!")
        while x > 0 and tries_1 < 2:
            playing is True
            next: int = int(input(" Choose 1 to go left to the ocean or choose 2 to go right to the forest:  "))
            if next == 1:
                ocean: int = int(input("You have chosen to go to the ocean. You want to explore but need to buy scuba gear for 3 points. Choose 1 to buy the gear or 2 to stay on land: "))
                if ocean == 1:
                    x -= 3
                    print(f"Yay {player} you swam underwater! Oh no, it looks like there is a whale ahead that you need to defeat. Use your sword and sidekick to help you.")
                    win: int = randint(1, 2)
                    if win == 1:
                        print("Yay! You defeated the enemy! You earned 2 point")  
                        x += 2
                    else:
                        print("Oh no! You were defeated by the enemy. You lost 2 points")
                        x -= 2
                elif ocean == 2:
                    print(f"Oh no {player}! There is a crab chasing you but you are stranded on land. You lost 1 point")
                    x -= 1
            elif next == 2:
                forest: int = int(input("You have chosen to enter the forest. It is getting cold outside but you can buy logs to start a fire. Choose 1 to buy logs and 2 to continue without:  "))
                if forest == 1:
                    x -= 2
                    win: int = randint(1, 2)
                    if win == 1:
                        print("You started a fire for warmth but ended up starting a forest fire. You lost 2 points")  
                        x -= 2
                    else:
                        print("Yay! You successfully built a fire to stay warm. You earned 3 points")
                        x += 3
                elif forest == 2:
                    win: int = randint(1, 2)
                    if win == 1:
                        print("You got frostbite and lost 3 points")  
                        x -= 3
                    else:
                        print("You were cold throughout the night, but were able to hide from enemies. You earned 1 point")
                        x += 1
            tries_1 += 1
            print(f"You currently have {x} points remaining")
        tries_3: int = 0
        while x > 0 and tries_3 < 1:  # Final battle
            playing is True
            print("Congrats on completing your second journey! Time for your final battle!")
            enemy: int = int(input("Congrats on making it this far! For your final mission you must correctly predict a coin flip to defeat the boss enemy. Guess heads by entering 1 and tails by entering 2: "))
            win: int = randint(1, 2)
            if win == enemy:
                print("Congrats you won 15 points and successfully beat the game!")
                x += 15
            elif win != enemy:
                print("Sorry, you lost 15 points and lost the game.")
                x -= 15
        tries_3 += 1
    return x


if __name__ == "__main__":
    main()