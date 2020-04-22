# -*- coding: utf-8-*-


# TEMA: Manejo de archivos

def run():
    with open('./manejo_de_archivos/numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

if __name__ == '__main__':
    run()