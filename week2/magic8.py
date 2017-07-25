import random as rd
"""
- Event Loops
- User I/O
- Random Module
Print a welcome screen to the user.
1. use the random module's `random.choice()` to choose a prediction (or with your own clever logic).
1. Display the result of the 8 ball.
1. Ask the user if they want to play agian.
1. Say Goodbye on exit.
"""


bizarro = rd.choice(['You shall be honored', 'Yes, indeed', 'Perhaps', 'Sometimes', 'If you apply yourself',
                         'Only on Tuesdays', 'Absolutely','By law, it is decreed', 'Didn\'t your mother tell you?',
                         'Emperor Mao agrees', 'Let is be', 'Under no circumstances', 'When you\'re wise',
                         'The President wills it so','On Mars only', 'After or before you die?', 'Wiser you should be'])

yes = ('Yes', 'Y', 'yes')
no = ('No', 'N', 'no')

def scelta():

    scelta1 = input('Type your question >>  ')


    if scelta != None :
        return bizarro
    elif input2('Do you want to continue?>> '):
        if input2 == yes:
            start()
    else:
        if input2 == no:
           exit()
        pass


def start():
    print('Welcome to the Magic 8 Ball')
    print('Where your future is our business')time.sleep(10)

    start_answ = input('Are you ready to begin? Y/N')

    if start_answ == 'y' or 'Y' or 'Yes' or 'yes':   # TODO: clean up later.
        scelta()
    else:
        start()


answer = input('Do you want to play again? >>  ')
    while answer != 'no':
        continue

start()

























