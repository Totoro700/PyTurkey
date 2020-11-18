# 
#        PyTurkey
# 
# 
# 
# ▀█▀ █░█ █▀█ █▄▀ █▀▀ █▄█ 
# ░█░ █▄█ █▀▄ █░█ ██▄ ░█░
# 
# 
# 
# 
# 
import time, sys, random, math

turkey =  0


def text(msg):
    msg = str(msg)
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.003)
    print('')

text('Welcome to PyTurkey!')
text('Type "help" for a list of commands you can use')



while True:
    cmd = input('')
    if cmd == 'help':
        text('Turkey commands:')
        text('help - Opens the Bot Command list')
        text('play - Play to get a chance to win turkey')
        text('turkey - Returns how much turkey you have')
        text('sell - Choose things you want to sell')
        text('exit - Exits this bot')
    elif cmd == '!coolPrint':
        text('Okay, what should we print?')
        acy = input('')
        text(acy)
    elif cmd == '!regularPrint':
        text('Okay, what should we print?')
        acy = input('')
        print(acy)
    elif cmd == 'exit':
        text('Data you entered(turkey, paper and others) will not be saved! Are you sure you want to exit? Y = Exit | N = Cancel')
        exitInput = input('')
        if exitInput == 'Y' or exitInput == 'y':
            text('Exiting . . .')
            exit()
        elif exitInput == 'N' or exitInput == 'n':
            continue
        else:
            text('That\'s not a valid answer')
            continue
    elif cmd == 'Hello' or cmd == 'hello' or cmd == 'Hello!' or cmd == 'hello!' or cmd == 'hi' or cmd == 'Hi' or cmd == 'hi!' or cmd == 'Hi!':
        text('Hi! Type "help" for a list of commands')
    elif cmd == 'play':
        text('To get turkey, answer this question:')
        text('Join(not add) these two numbers:')
        numO = str(random.uniform(3, 50))
        numT = str(random.uniform(3, 13))
        ans = numO+numT
        text(numO)
        text('And')
        text(numT)
        text('What\'s the answer?')
        uAns = str(input(''))
        if uAns == ans:
            turkey = turkey + 1
            text('Correct!')
            text('You have '+str(turkey)+' coin(s) now!')
            continue
        else:
            text('Incorrect!')
            turkey = turkey - 1
            text('You have '+str(turkey)+' coin(s) left!')
            continue
    elif cmd == 'turkey':
        text('You have '+str(turkey)+' turkey(s)')
    elif cmd == 'sell':
        print('No selling turkey!')
    elif cmd == 'PyTurkey':
        text('▀█▀ █░█ █▀█ █▄▀ █▀▀ █▄█ \n░█░ █▄█ █▀▄ █░█ ██▄ ░█░')
    else:
        continue
