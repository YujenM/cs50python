from random import randint
import cowsay
# rock paper siccsor
def main():
    instruction()
    game=""
    if game==True:
        instruction()
# how to play
def instruction():
    print("    Rock-Paper-Sicssor   ")
    print(start_game())
    print("Keys of the Game")
    print("1=✊rock")
    print("2=✋paper")
    print("3=✌️ siccsor")
    how_many_round()
    exit()
# to start the game
def start_game():
    while True:
        user=input("Press s to start the game: ").lower()
        if user=="s":
            game=True
            return game
        else:
            print("Press s to start the game")
# taking user input
def user_input():
    while True:
        user=int(input("Enter number from 1-3: "))
        if user==1 or user==2 or user==3:
            break
        else:
            print("Enter from 1-3")
    if user==1:
         print("✊")
    if user==2:
         print("✋")
    if user==3:
         print("✌️")
    computer=randint(1,3)
    if computer==1:
        print("✊")
    if computer==2:
        print("✋")
    if computer==3:
        print("✌️")
    print(wining(user,computer))
# see who is wining or draw
def wining(user,computer):
    if user==computer:
        return ("Tie")
    if user==1 and computer==2:
        return ("computer wins")
    if user==2 and computer==3:
        return ("computer wins")
    if user==3 and computer==1:
        return ("computer wins")
    if user==1 and computer==3:
        return ("user wins")
    if user==3 and computer==2:
        return ("user wins")
    if user==2 and computer==1:
        return ("user wins")
# how many games to play
def how_many_round():
    try:
        round=0
        rounds=int(input("How many rounds do you want to play?: "))
        while True:
            if round==rounds:
                break
            elif round!=rounds:
                user_input()
                round+=1
    except ValueError:
        print("Enter integer")
#thanks for playing
def exit():
    cowsay.cow("Thanks for playing")
if __name__=="__main__":
    main()