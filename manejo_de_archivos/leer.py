# -*- coding: utf-8-*-


# TEMA: Manejo de archivos

def run():
    counter = 0
    with open('./manejo_de_archivos/lorem.txt', 'r') as f:
        # print(f.readlines()) #lee el texto existente y separa los saltos de linea con \n
        for line in f:
            counter += line.count('dolor')
    print('lorem se encuentra {} en el texto'.format(counter))

if __name__ == '__main__':
    run()
    