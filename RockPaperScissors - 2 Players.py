# Rock, Paper Scissors game

print('This is the rock, paper, scissors game. \n')
print()

quit = False

while True:    
    Player1 = input('Player1 - Enter rock, paper, scissors or quit: ')
    print('Player1 selected ', Player1)
    print()
    Player2 = input('Player2 - Enter rock, paper, scissors or quit: ')
    print('Player2 selected ', Player2)
    print()
    
    if Player1 == 'quit' or Player2 == 'quit':
        break
    elif (Player1!='rock' and Player1!='paper' and Player1!='scissors' and Player1!='quit') or (Player2!='rock' and Player2!='paper' and Player2!='scissors' and Player2!='quit'):
        print('Invalid input! You have not entered rock, paper or scissors, try again.')
    else:
        if Player1 == Player2:
            print("It's a tie")
            print()
        if Player1 == 'rock' and Player2 == 'scissors':
            print('Rock beats scissors')
            print('Player1 wins \n')
        if Player2 == 'rock' and Player1 == 'scissors':
            print('Rock beats scissors')
            print('Player2 wins \n')
        if Player1 == 'scissors' and Player2 == 'paper':
            print('Scissors beats paper')
            print('Player1 wins \n')
        if Player2 == 'scissors' and Player1 == 'paper':
            print('Scissors beats paper')
            print('Player2 wins\n')
        if Player1 == 'paper' and Player2 == 'rock':
            print('Paper beats rock')
            print('Player1 wins')
        if Player2 == 'paper' and Player1 == 'rock':
            print('Paper beats rock')
            print('Player2 wins\n')
                      
