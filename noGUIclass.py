import numpy as np
import random


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

    def win_check(self, state, player):
        for i in range(self.field_size):
            counter_goriz = 0
            counter_vert = 0
            counter_diag1 = 0
            counter_diag2 = 0
            sec_i = self.field_size - 1
            for j in range(self.field_size):
                if state[i][j] == player and state[i][j + 1] == player:
                    counter_goriz += 1
                else:
                    counter_goriz = 0
                if state[j][i] == player and state[j + 1][i] == player:
                    counter_vert += 1
                else:
                    counter_vert = 0
                if state[j][j] == player :
                    counter_diag1 += 1
                else:
                    counter_diag1 = 0
                if state[j][sec_i] == player:
                    counter_diag2 += 1
                else:
                    counter_diag2 = 0
                sec_i -= 1
                print(counter_goriz, counter_vert, counter_diag1, counter_diag2, '\n')
            if counter_goriz >= self.score or counter_vert >= self.score \
                    or counter_diag1 >= self.score \
                    or counter_diag2 >= self.score:
                return True

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
        else:
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
        print(depth)
        if depth == self.field_size ** 2:
            print('ok')
            x = random.randint(0, self.field_size - 1)
            y = random.randint(0, self.field_size - 1)
        else:
            print('ok')
            move = self.minimax(self.k, 3, self.AI)
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
                chose(self.field_size, self.k, self.AI)
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
