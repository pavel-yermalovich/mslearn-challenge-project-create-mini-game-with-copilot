import random

# declare integer variable games
games = 0
won = 0

while True:
    while True:
        user_input = input('Enter rock, paper, or scissors: ').lower()
        if user_input in ['rock', 'paper', 'scissors']:
            break
        else:
            print('Invalid input. Please try again.')

    computer_input = random.choice(['rock', 'paper', 'scissors'])
    if user_input == computer_input:
        print('Tie!')
    elif (user_input == 'rock' and computer_input == 'scissors' 
        or user_input == 'scissors' and computer_input == 'paper' or
        user_input == 'paper' and computer_input == 'rock'):
        print('You win!')
        won += 1
    else:
        print('You lose!')

    games += 1

    play_again = input('Play again? (yes/no): ').lower()
    if play_again == 'yes':
        continue
    else:
        print(f'You played {games} games and won {won} games.')
        break

