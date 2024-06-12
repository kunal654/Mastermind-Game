import random

def generate_number(length):
    return ''.join(random.choices('0123456789', k=length))

def get_feedback(secret, guess):
    correct_positions = sum(1 for s, g in zip(secret, guess) if s == g)
    correct_digits = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - correct_positions
    return correct_positions, correct_digits

def play_round(player_name, secret):
    attempts = 0
    while True:
        guess = input(f"{player_name}, enter your guess: ")
        attempts += 1
        correct_positions, correct_digits = get_feedback(secret, guess)
        print(f"Correct digits in correct positions: {correct_positions}")
        print(f"Correct digits but in wrong positions: {correct_digits}")
        if guess == secret:
            print(f"{player_name} guessed the number correctly in {attempts} attempts!")
            return attempts

def mastermind_game():
    number_length = int(input("Enter the length of the number to guess: "))
    
    # Round 1: Player 1 sets the number
    print("Round 1: Player 1 sets the number")
    secret_number1 = input("Player 1, enter the number for Player 2 to guess (keep it secret): ")
    attempts_player2 = play_round("Player 2", secret_number1)
    
    # Round 2: Player 2 sets the number
    print("Round 2: Player 2 sets the number")
    secret_number2 = input("Player 2, enter the number for Player 1 to guess (keep it secret): ")
    attempts_player1 = play_round("Player 1", secret_number2)
    
    # Determine the winner
    print("\nGame Over!")
    print(f"Player 2 attempts: {attempts_player2}")
    print(f"Player 1 attempts: {attempts_player1}")
    
    if attempts_player1 < attempts_player2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    mastermind_game()
