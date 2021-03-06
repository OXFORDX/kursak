import numpy as np
import random
from math import sqrt


class tic_tac_toe:
    def __init__(self, size, score):
        self.field_size = size
        self.k = np.zeros([size, size], dtype=int)
        self.checker = False
        self.HUMAN = 1
        self.AI = -1
        self.score = score

    def field_print(self):
        print(np.array(self.k))

    def end_game(self, state):
        return self.win_check(state, self.HUMAN) or self.win_check(state, self.AI)

    def diagonals_check(self, arr, player):
        for i, j in enumerate(arr[0]):
            d1 = 0
            d2 = 0
            d3 = 0
            d4 = 0
            for k in range(4):
                try:

                    if arr[k][i + k] == player and arr[k + 1][i + k + 1] == player:
                        d1 += 1
                    if arr[i + k][k] == player and arr[i + k + 1][k + 1] == player:
                        d2 += 1
                    if arr[k][i - k] == player and arr[k + 1][i - k - 1] == player:
                        if i - k >= 0 and i - k - 1 >= 0:
                            d3 += 1

                    if arr[k + 1][i - k] == player and arr[k + 2][i - k - 1] == player:
                        if i - k >=0 and i - k - 1>=0:
                            d4 += 1



                except IndexError:
                    pass
            print(d1 + 1, d2 + 1, d3 + 1, d4 + 1)
            if d1 + 1 > self.score - 1 or d2 + 1 > self.score - 1 or d3 + 1 > self.score - 1 or d4 + 1 > self.score - 1:
                return True
        return False

    def win_check(self, state, player):
        for i in range(self.field_size):
            counter_goriz = 0
            counter_vert = 0
            for j in range(self.field_size):
                try:
                    if state[i][j] == player and state[i][j + 1] == player:
                        counter_goriz += 1
                    if state[j][i] == player and state[j + 1][i] == player:
                        counter_vert += 1
                except IndexError:
                    pass
            if counter_goriz + 1 >= self.score or counter_vert + 1 >= self.score:
                return True
        print(self.diagonals_check(state, player))
        return self.diagonals_check(state, player)

    def empty_cells(self, state):
        cells = []

        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def draw(self):
        for i in self.k:
            for j in i:
                if not j:
                    return False
        return True

    def evaluate(self, state):
        if self.win_check(state, self.AI):
            score = +1
        elif self.win_check(state, self.HUMAN):
            score = -1
        else
            score = 0

        return score

    def minimax(self, state, depth, player):
        if player == self.AI:
            best = [-1, -1, -999999]
        else:
            best = [-1, -1, 999999]

        if depth == 0 or self.end_game(state):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.AI:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def ai_turn(self):
        depth = len(self.empty_cells(self.k))
        if depth == 0 or self.end_game(self.k):
            return
        if depth == self.field_size ** 2:
            x = random.randint(0, self.field_size - 1)
            y = random.randint(0, self.field_size - 1)
        else:
            move = self.minimax(self.k, self.score, self.AI)
            x, y = move[0], move[1]

        return x, y

    def startgame(self):
        self.checker = False
        self.field_print()

        def chose(field_size, k, xo):
            print('=' + str(xo) + '=')
            x, y = int(input('i:')), int(input('j:'))
            if not k[x][y]:
                k[x][y] = xo
                return
            print('Incorrect position!')
            chose(field_size, k, xo)

        z = 0
        while True:
            if self.draw():
                print('Draw!')
                break
            if z % 2 == 0:
                x, y = self.ai_turn()
                self.k[x][y] = self.AI
                self.field_print()
                if self.win_check(self.k, self.AI):
                    print('X win!', 3)
                    break
                z += 1
            elif z % 2 == 1:
                chose(self.field_size, self.k, self.HUMAN)
                self.field_print()
                if self.win_check(self.k, self.HUMAN):
                    print('O win!')
                    break
                z += 1
