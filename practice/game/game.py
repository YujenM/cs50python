import random
while True:
    try:
        user=int(input("Level: "))
        if user<=0:
            continue
        else:
            break
    except:
        pass
number=random.randint(1,user)
while True:
    try:
        guess=int(input("Guess: "))
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too Large!")
        else:
            print("Just right!")
            break
    except:
        pass
