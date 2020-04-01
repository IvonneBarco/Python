# -*- coding: utf-8 -*-

import turtle

# Funciones: Ejm: Turtle

def main():
    window = turtle.Screen()
    ivonne = turtle.Turtle()

    make_square(ivonne)

    turtle.mainloop()

def make_square(ivonne):
    lenght = int(raw_input('Tamaño del cuadrado: '))

    for i in range(4):
         make_line_and_turn(ivonne, 100)

def make_line_and_turn(ivonne, length):
    ivonne.forward(length)
    ivonne.left(90)

if __name__ == '__main__':
  main()

turtle.mainloop()