import random
import enum


class Choice(enum.IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


Victories = {
    Choice.Scissors: [Choice.Lizard, Choice.Paper],
    Choice.Paper: [Choice.Spock, Choice.Rock],
    Choice.Rock: [Choice.Lizard, Choice.Scissors],
    Choice.Lizard: [Choice.Spock, Choice.Paper],
    Choice.Spock: [Choice.Scissors, Choice.Rock],
}


def user_choice():
    choice = [f'{i.name} - {i.value}' for i in Choice]
    choices_str = ', '.join(choice)
    start = int(input(f'Make your choice ({choices_str}): '))
    action = Choice(start)
    return action


def computer_choice():
    selection = random.randint(0, len(Choice) - 1)
    action = Choice(selection)
    return action


def winner_selection(user_choice, computer_choice):
    defeats = Victories[user_choice]
    if user_choice == computer_choice:
        print(f'You and computer chose {user_choice.name}. It\'s a tie!')
    elif computer_choice in defeats:
        print(f'You win! Computer chose {computer_choice.name}.')
    else:
        print(f'You lose. Computer chose {computer_choice.name}.')


while True:
    try:
        user = user_choice()
    except ValueError as e:
        range_str = f'[0, {len(Choice) - 1}]'
        print(f'Error! Select number from range {range_str}.')
        continue

    computer = computer_choice()
    winner_selection(user, computer)

    play_again = input('Rematch? Yes - "y", No - "n": ')
    if play_again.lower() != 'y':
        break

