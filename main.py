# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
number = random.randint(1,50)
attempt = 0
while attempt <6:
    guess = int(input('Число '))
    attempt +=1

    if guess < number:
        print('больше')
    if guess > number:
        print('меньше')
    if guess == number:
        print(f'число угадано с {attempt} попытки')
        break
    if guess != 0 and attempt == 6:
        print(f'не вышло, {number} был загаданным числом')
        break


