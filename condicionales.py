# -*- coding: utf-8-*-


# TEMA: Condicionales


def say_hello():
    print('C O N D I C I O N A L E S')
    print('')

    age = float(raw_input('Cuál es tu edad: '))

    if age > 18:
        print('Hola señor')
    else:
        print('Hola niño')


if __name__ == '__main__':
    say_hello()
    