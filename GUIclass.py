import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename
from noGUIclass import tic_tac_toe
import os
import json

AI = 1
HUMAN = -1
O = "O"
X = "X"
BLANK = ""


class Main(tk.Frame):
    def __init__(self, root):
        global size

        size = 0
        super().__init__(root)
        self.init_main()

    def init_main(self):
        welcome = tk.Frame(bg='white', bd=5).pack(side=tk.TOP)
        Label = tk.Label(welcome, text='Ласкаво прошу до гри Хрестики-Нулики!\nВиберіть розмірність поля:',
                         font='Verdana 12 bold', fg='white', bg='gray').pack(side=tk.TOP, pady=10)
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        tk.Label(toolbar, text='OPTIONS:', bg='light gray', font='Arial 12 bold').pack(side=tk.LEFT, pady=0)
        tk.Button(toolbar, text='Load...', bg='light gray', font='Arial 12 bold', command=self.OpenFile).pack(
            side=tk.LEFT, padx=20)
        tk.Button(toolbar, text='3x3', bg='light gray', font='Arial 12 bold', command=self.three).pack(
            side=tk.TOP, pady=0)
        tk.Button(toolbar, text='4x4', bg='light gray', font='Arial 12 bold', command=self.four).pack(side=tk.TOP,
                                                                                                      pady=0)
        tk.Button(toolbar, text='5x5', bg='light gray', font='Arial 12 bold', command=self.five).pack(side=tk.TOP,
                                                                                                      pady=0)
        label = tk.Label(text="Правила:\n1) Перший ходить комп'ютер.\n2) Зібрати 3 в ряд хрестиків або нуликів\n",
                         font='Arial 12 bold').pack(side=tk.LEFT)

    def three(self):
        global size
        size = 3
        Child()

    def four(self):
        global size
        size = 4
        Child()

    def five(self):
        global size
        size = 5
        Child()

    def OpenFile(self):
        global name
        name = askopenfilename(initialdir=os.getcwd(),
                               filetypes=(("Json files", "*.json"), ("All Files", "*.*")),
                               title="Choose a file."
                               )
        print(name)
        try:
            with open(name, 'r') as UseFile:
                print(UseFile.read())
        except:
            print("No file exists")


class Child(tk.Toplevel):
    def __init__(self):
        global size
        global counter
        global name
        counter = 0
        super().__init__(root)
        self.ttt = tic_tac_toe(size, 3)
        self.turn = AI

        self.board = []

        for i in range(size):

            l = []

            line = tk.Frame(self)
            line.pack()

            for j in range(size):
                button_text = tk.StringVar(line, BLANK)
                button = tk.Button(
                    line,
                    textvariable=button_text,
                    width=10,
                    height=5,
                    font='Times 10 bold',
                    command=self.press(i, j)
                )
                button.pack(side=tk.LEFT)

                l.append((button_text, button))

            self.board.append(l)
        line = tk.Frame(self).pack()
        tk.Button(line, text='Save...', bg='light gray', font='Arial 12 bold', command=)
        x, y = self.ttt.ai_turn()
        button_text, button = self.board[x][y]
        button.invoke()

    def save_file(self):
        pass

    def press(self, i, j):
        def real_press():
            global counter
            counter += 1
            button_text, button = self.board[i][j]
            if self.ttt.k[i][j]:
                return

            if self.turn == AI:
                button_text.set(O)
                self.ttt.k[i][j] = 1

                if self.ttt.win_check(self.ttt.k, AI):
                    print(self.ttt.k)
                    messagebox.showinfo('Інфо', 'Противник виграв!')
                    Child.destroy(self)
                if not len(self.ttt.empty_cells(self.ttt.k)):
                    messagebox.showinfo('Інфо.'.format(HUMAN), 'Нічия')
                    Child.destroy(self)
                self.turn = HUMAN

            elif self.turn == HUMAN:
                button_text.set(X)
                self.ttt.k[i][j] = -1

                if self.ttt.win_check(self.ttt.k, HUMAN):
                    messagebox.showinfo('Інфо'.format(HUMAN), 'Ви виграли!')
                    Child.destroy(self)
                if not len(self.ttt.empty_cells(self.ttt.k)):
                    messagebox.showinfo('Інфо'.format(HUMAN), 'Противник виграв!')
                    Child.destroy(self)
                self.turn = AI
                x, y = self.ttt.ai_turn()
                print(self.ttt.k)
                print(x, y)
                button_text, button = self.board[x][y]
                print(button_text, button)
                button.invoke()

        return real_press


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("TicTacToe")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
