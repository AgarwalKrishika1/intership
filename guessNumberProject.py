import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        #f-string to add variable in statement
        guess = int(input(f'Guess number between 1 and {x}  '))
        if guess < random_number:
            print("guess another , too low")
        elif guess > random_number:
            print("guess another, too high")

    print(f'yaya guess {random_number}  correct')

y = int(input("enter number for guess "))
guess(y)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'{guess} too high(H), too low(L), or correct(C)'.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay! coorect {guess}')
y = int(input("enter number for guess "))
computer_guess(y)