# Rock, Paper Scissors game

import random

quit = False

print('This is the rock, paper, scissors game. \n')
print()

while True:
    bot = random.choice(['rock', 'paper', 'scissors', 'quit'])
    Player = input('Player - Type rock, paper, scissors or quit: ')
    print('Player selected', Player)
    print()
    
    if Player == 'quit' or bot == 'quit':
        if bot == 'quit':
            print('Bot selected to ',bot)
        break         
    elif Player != 'rock' and Player != 'paper' and Player != 'scissors' and Player != quit:
            print('Invalid input! You have not entered rock, paper or scissors, try again.\n')     
    else:                   
        if Player == bot:
            print("It's a tie \n")                        
        if Player == 'rock' and bot == 'scissors':
            print('Rock beats scissors')
            print('Player wins \n')            
        if bot == 'rock' and Player == 'scissors':
            print('Rock beats scissors')
            print('bot wins \n')            
        if Player == 'scissors' and bot == 'paper':
            print('Scissors beats paper')
            print('Player wins \n')            
        if bot == 'scissors' and Player == 'paper':
            print('Scissors beats paper')
            print('Bot wins\n')
        if Player == 'paper' and bot == 'rock':
            print('Paper beats rock')
            print('Bot wins')
        if bot == 'paper' and Player == 'rock':
            print('Paper beats rock')
            print('Bot wins\n')               
