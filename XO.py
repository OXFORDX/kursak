from random import *
import time

field_size = int(input('Enter size of field:'))


def matgen(field_size):
    k = []
    for i in range(1, field_size ** 2, field_size):
        row = []
        for j in range(i, i + field_size):
            row.append(j)
        k.append(row)
    return k


k = matgen(field_size)


def field_print(field_size):
    global k
    print('=' * (4 * field_size - 3))
    for i in range(field_size):
        for j in range(field_size):
            if j == field_size - 1:
                print(k[i][j])
                break
            print(k[i][j], end=' | ')
        print('=' * (4 * field_size - 3))


field_print(field_size)


def addelem():
    global k
    z = 0

    def some(xo):
        print('=' + str(xo) + '=')
        y = int(input('Number:'))
        for i in range(field_size):
            for j in range(field_size):
                if k[i][j] == y:
                    k[i][j] = str(xo)
                    field_print(field_size)

    while True:
        if z % 2 == 0:
            some('X')
            z += 1

        elif z % 2 == 1:
            some('O')
            z += 1


addelem()
