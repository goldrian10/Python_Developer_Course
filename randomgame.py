import sys
import random


def guess(num):
    result = False
    if num == random_num:
        result = True
    return result


hit = False
begin = int(sys.argv[1])
finish = int(sys.argv[2])
random_num = random.randint(begin, finish)

while not hit:
    try:
        guess_num = int(input(f'Adivine un numero entre {begin} y {finish}\n'))
    except ValueError:
        print('Por favor escriba un numero')
        continue

    if guess_num < begin or guess_num > finish:
        print(f'Por Favor elija un numero entre {begin} y {finish}')
        continue
    hit = guess(guess_num)
    print(f'Error, intente de nuevo!')

print(f'Felicidades el numero era {random_num}')
