class tic_tac_toe:
    def __init__(self, size):
        print('Welcome to the tic_tac_toe creator')
        self.field_size = size
        self.k = []
        self.checker = False

    def matgen(self):
        ''''Matrix generation in a row: [1...n]
                                          ...
                                      [n + 1...n + n]'''
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

    def score_check(self, xo):

        for i in range(self.field_size):
            counter_goriz = 0
            counter_vert = 0
            counter_diag1 = 0
            counter_diag2 = 0
            sec_i = self.field_size - 1
            for j in range(self.field_size):
                if self.k[i][j] == str(xo):
                    counter_goriz += 1
                if self.k[j][i] == str(xo):
                    counter_vert += 1
                if self.k[j][j] == str(xo):
                    counter_diag1 += 1
                if self.k[j][sec_i] == str(xo):
                    counter_diag2 += 1
                sec_i -= 1
            if counter_goriz == self.field_size or counter_vert == self.field_size \
                    or counter_diag1 == self.field_size \
                    or counter_diag2 == self.field_size:
                return True

    def draw(self):
        for i in self.k:
            for j in i:
                if isinstance(j, int):
                    return False
        return True

    def startgame(self):
        self.checker = False
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
            if self.draw():
                print('Draw!')
                break
            if z % 2 == 0:
                chose(self.field_size, self.k, 'X')
                self.field_print()
                if self.score_check('X'):
                    print('X win!')
                    break
                z += 1
            elif z % 2 == 1:
                chose(self.field_size, self.k, 'O')
                self.field_print()
                if self.score_check('O'):
                    print('O win!')
                    break
                z += 1
