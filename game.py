import random #RANDOM MODULE

randNum = random.randint(1,100)
userGuess = None
guesses = 0
print('-----WELCOME TO THE PERFECT GUESS-----\n')
while(userGuess != randNum):
    userGuess = int(input('Enter Number: '))
    guesses += 1
    if (userGuess == randNum):
        print('\n++++ Hurray You Guessed The Right Number ++++\n')
    else:
        if (userGuess > randNum):
            print('\nYou Guessed It Wrong! Choose Smaller Number..\n')
        else:
            print('\nYou Gussed It Wrong! Choose Larger Number..\n')

print(f'You Gussed The Number In {guesses} Gusses')

with open ('highscore.txt', 'r') as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print('\n************You have just broken the High Score************')
    with open ('highscore.txt', 'w') as f:
        f.write(str(guesses))