class tic_tac_toe:
    def __init__(self):
        print('Welcome to the tic_tac_toe creator')
        self.field_size = 0
        self.k = []

    def matgen(self):
        ''''Matrix generation in a row: [1...n]
                                          ...
                                      [n + 1...n + n]'''
        size = int(input('Enter size of field:'))
        self.field_size = size
        for i in range(1, self.field_size ** 2, self.field_size):
            row = []
            for j in range(i, i + self.field_size):
                row.append(j)
            self.k.append(row)
        return self.k

    def field_print(self):
        'Problems with number 10 100 1000'
        print('=' * (4 * self.field_size - 3))
        for i in range(self.field_size):
            for j in range(self.field_size):
                if j == self.field_size - 1:
                    print(self.k[i][j])
                    break
                print(self.k[i][j], end=' | ')
            print('=' * (4 * self.field_size - 3))

    def startgame(self):
        self.matgen()
        self.field_print()

        def chose(field_size, k, xo):
            print('=' + str(xo) + '=')
            y = int(input('Number:'))
            for i in range(field_size):
                for j in range(field_size):
                    if k[i][j] == y:
                        k[i][j] = str(xo)

        z = 0
        while True:
            if z % 2 == 0:
                chose(self.field_size, self.k, 'X')
                self.field_print()
                z += 1
            elif z % 2 == 1:
                chose(self.field_size, self.k, 'O')
                self.field_print()
                z += 1
