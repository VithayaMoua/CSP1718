import random

def roll(sides=6):
    num_rolled = random.randint(1,sides) #generate random number between 1 and sides (default to 6)
    return num_rolled #return the random number
    
def main():
    sides = 6 #store the number 6 in a variable
    rolling = True #store True in a variable
    while rolling:
        roll_again = raw_input("Are you ready to roll? ENTER=Roll. Q=Quit. ") #generate message after a roll
        if roll_again.lower() !="q": #
            num_rolled = roll(sides) #generate number same as side
            print("You rolled a", num_rolled) #print random number rolled
        else:
            rolling = False #store False in a variable
            
    print("Thanks for playing.")

main()