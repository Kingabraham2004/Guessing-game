import random

def play_game():
    randomly_generated_number = random.randint(1, 999)
    score = 100
    number_of_guesses = 0

    while score > 0:
        try:
            user_guess = int(input('Guess a number between 1 and 999: \n'))
            number_of_guesses += 1
            if user_guess == randomly_generated_number:
                return f'you guessed correctly, the number is {randomly_generated_number}. you did it in {number_of_guesses} and your score is {score}%'
            elif user_guess - randomly_generated_number <= 10:
                print(' You are almost there, Go higher/lower')
                score -= 2
            elif user_guess - randomly_generated_number <= 50:
                print('You are getting close, a bit higher/lower')
                score -= 3
            elif user_guess - randomly_generated_number <= 100:
                print('Still not there, Go higher/lower')
                score -= 7
            elif user_guess - randomly_generated_number <= 200:
                print('INCORRECT! Go much higher/lower')
                score -= 10
            else:
                score -= 1
                print('You are basically there. Just steps away. Try higher/lower')
        except ValueError:
            print('Invalid Input. Please Enter a number between 1 and 999')
            return f'You have failed the game. Your score is {score}%. The number was {randomly_generated_number}.please play again, thanks!'
play_game()
