# -*- coding: utf-8-*-

from lamp import Lamp, Foco

# Archivo con la lógica

def run():
    lamp = Lamp(_is_turned_on = False)

    while True:
        command = str(raw_input('''
            ¿Que deseas hacer?

            [p]render 
            [a]pagar
            [s]alir       
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()