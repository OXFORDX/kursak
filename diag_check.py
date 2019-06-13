import numpy as np

arr = np.random.randint(2, size=(4, 4))
print(arr)
diag1 = []
diag2 = []
for i, j in enumerate(arr[0]):
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    for k in range(4):
        try:
            if arr[k][i + k] and arr[k + 1][i + k + 1]:
                d1 += 1
            if arr[i + k][k] and arr[i + k + 1][k + 1]:
                d2 += 1
            if arr[k][i - k] and arr[k + 1][i - k - 1]:
                d3 += 1

            if arr[k + 1][i - k] and arr[k + 2][i - k - 1]:
                d4 += 1

        except IndexError:
            pass
    print('---')
    print('d1: ', d1 + 1)
    print('d2: ', d2 + 1)
    print('d3: ', d3 + 1)
    print('d4: ', d4 + 1)
    print('---')