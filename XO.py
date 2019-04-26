from random import *
import time

field_size = int(input('Enter size of field:'))


def matgen(field_size):
    k = []
    i = 1
    while i != field_size - 1:
        for j in range(field_size):
            k.append(j)
            i += 1
        print(i)
    return k


print(matgen(field_size))

# start_time = time.time()
#
#
# def matprint(field_size):
#     print('=' * (4 * field_size - 3))
#     for i in range(field_size):
#         for j in range(field_size):
#             if j == field_size - 1:
#                 print(k[i][j])
#                 break
#             print(k[i][j], end=' | ')
#         print('=' * (4 * field_size - 3))
#
#
# def addelem():
#     z = 0
#
#     while True:
#         if z % 2 == 0:
#             print('=X=')
#             x, y = int(input('enter i:')) - 1, int(input('enter j:')) - 1
#             if k[x][y] != ' ':
#                 print('This cell is already taken')
#                 break
#             k[x][y] = 'X'
#             matprint()
#             z += 1
#
#         elif z % 2 == 1:
#             print('=O=')
#             x, y = int(input('enter i:')) - 1, int(input('enter j:')) - 1
#             if k[x][y] != ' ':
#                 print('This cell is already taken')
#                 break
#             k[x][y] = 'O'
#             matprint()
#             z += 1
#         if z == 9:
#             print('===Draw===')
#             return
#
#
# matprint(field_size)
