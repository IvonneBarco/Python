# -*- coding: utf-8-*-


# TEMA: Calcular si un número es primo con Python

def is_prime_(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True

def run():
    number = int(raw_input('Escribe un número: '))
    result = is_prime_(number)

    if result is True:
        print('Tu número es primo')
    else:
        print('Tu número NO es primo')


if __name__ == '__main__':
    run()

