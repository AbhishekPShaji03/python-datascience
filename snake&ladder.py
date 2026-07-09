import random

position = 0
start = False

snakes = {17:7,54:34,62:19,98:16}
ladders = {3:22,8:26,20:38,28:84}

while position < 100:
    input("Press Enter to roll the dice ...")
    dice = random.randint(1,6)
    print("Dice:",dice)

    if not start:
        if dice == 1:
            start = True
            print("Game started")
        else:
            print("you need to get 1 to start the game")
            continue
        
    position += dice

    if position in ladders:
        print("You got a ladder")
        position = ladders[position]

    elif position in snakes:
        print("oh noo! snake bite")
        position = snakes[position]

    if position > 100:
        position -= dice

    print("current position:",position)        

if position == 100:
    print("Congratulations! you won ")