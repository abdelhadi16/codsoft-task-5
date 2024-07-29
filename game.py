
import random

def bot_choice():
    options = ['rock', 'paper', 'scissors']
    choice = random.choice(options)
    return choice

def human_tracker(h):
    return h + 1

def bot_tracker(b):
    return b + 1

print("Welcome to Rock-Paper-Scissors Game")
print("------------------------------------")
print("Wanna play?!")
print("1. yes or 2. yes")
input("Click any key: ")
play = True
rounds = ["first", "second", "third", "fourth", "fifth", "sixth"]
while play:
    x = 0
    h = 0
    b = 0
    while h != 3 and b != 3: 
        print("The", rounds[x], "round starts:")
        print("Choose your hand:")
        print("1. rock")
        print("2. paper")
        print("3. scissors")
        choice = int(input("Enter your choice: "))
        bot_choix = bot_choice()

        if choice in [1, 2, 3]:  
            human_choice = ['rock', 'paper', 'scissors'][choice - 1]

            # Tie cases
            if human_choice == bot_choix:
                print(f"You chose {human_choice} and the bot chose {bot_choix}. it's a tie.")
                print(f"You: {h} - The bot: {b}")
            else:
                # Win cases
                if (choice == 1 and bot_choix == 'scissors') or \
                   (choice == 2 and bot_choix == 'rock') or \
                   (choice == 3 and bot_choix == 'paper'):
                    print(f"You chose {human_choice} and the bot chose {bot_choix}.")
                    print(f"YOU WON THE {rounds[x]} ROUND!!")
                    h = human_tracker(h)
                else:
                    # Loss cases
                    print(f"you chose {human_choice} and the bot chose {bot_choix}.")
                    print(f"yOU LOST THE {rounds[x]} ROUND!!")
                    b = bot_tracker(b)

                print(f"you: {h} - the bot: {b}")
                x += 1

        else:
            print("invalid choice, try again")
  

    if h == 3:
        print("you won the game!")
        print(f"you: {h} - the bot: {b}")
    elif b == 3:
        print("you lost the game and the bot won!")
        print(f"You: {h} - The bot: {b}")

    print("do you wanna play again?")
    print("1. YES")
    print("2. NO and quit")
    
    replay = 0
    while replay not in [1, 2]:  
        replay = int(input("Enter your choice (1 or 2): "))
        
    if replay == 1:
        continue
    elif replay == 2:
        print("Bye, see you!!")
        break
