import random
from playsound import playsound

# Stone Paper Kenchi or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='p':
            return True
        elif you=='k':
            return False
     
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='k':
            return True
        elif you=='s':
            return False
    
    # Check for all possibilities when computer chose g
    elif comp == 'k':
        if you=='s':
            return True
        elif you=='p':
            return False

print("Comp Turn: Stone Paper or Kenchi? \n")
print("\n For Kenchi choose k \n For Stone choose s \n For Paper choose p\n")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'k'

you = input("Your Turn: Stone Paper or Kenchi?\n")


while you != "k" and you != "s" and you != "p":
    print("Please choose from 's', 'k' and 'p' \n")
    you = input("Your Turn: Stone Paper or Kenchi?\n")

a = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("Match Tied!")
    playsound('positive.mp3')
elif a:
    print("You Win!")
    playsound('wow.mp3')
else:
    print("You Lose!")
    playsound('negative.mp3')