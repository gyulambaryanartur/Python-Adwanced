import random as rd
import os


class Minesweeper:
    def __init__(self, length: int, heigth: int, countwipe: int):
        self.length = length
        self.heigth = heigth
        self.countwipe = countwipe
        self.countelement = set()
        self.x = 0
        self.y = 0

    def matrix_create(self):
        matr = [['.' for i in range(self.length)] for j in range(self.heigth)]
        return matr

    def data_validation(self):
        while True:
            if isinstance(self.heigth, int) and isinstance(self.length, int) and isinstance(self.countwipe, int) and \
                isinstance(self.x, int) and isinstance(self.y, int) and self.heigth*self.length >= self.countwipe and self.heigth>self.y \
                    and self.length>self.x:
                break
            else:
                print("Put correct values!!")
                exit(0)

    def put_bomb(self):
        self.data_validation()
        matrix = self.matrix_create()
        row = 0
        col = 0

        while self.countwipe > 0:
            row = rd.randint(0, self.heigth-1)
            col = rd.randint(0, self.length-1)
            matrix[row][col] = '*'
            self.countelement.add((col, row))

            if len(self.countelement) == self.countwipe:
                break

            else:
                continue
        return matrix

    def is_bomb(self, x, y):
        self.x = x
        self.y = y
        self.data_validation()
        self.put_bomb()
        bset = {(x, y)}
        if bset.issubset(self.countelement):
            return f'the provided cell contains bomb'
        else:
            return f'the provided cell does not  contains bomb'

    def number_of_bombs(self, x, y):
        self.x = x
        self.y = y
        self.data_validation()
        self.put_bomb()
        numberofbomb = 0
        bset = {(x, y-1)}
        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x, y+1)}
        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x-1, y)}

        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x+1, y)}

        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x+1, y-1)}

        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x+1, y+1)}

        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x-1, y+1)}

        if bset.issubset(self.countelement):
            numberofbomb += 1
        bset = {(x-1, y-1)}
        if bset.issubset(self.countelement):
            numberofbomb += 1

        return f'number of bombs nearby to the provided cell:{numberofbomb}'

    def save(self, fname: str):

        matrix = self.put_bomb()
        with open(fname, 'w') as fd:
            for row in matrix:
                fd.write(' '.join(row))
                fd.write('\n')


if __name__ == "__main__":
    curdir = os.getcwd()
    print(curdir)
    a = Minesweeper(10, 12, 120)
    a.save(f'{curdir}\\txtt.txt')
    print(a.is_bomb(6, 7))
    print(a.number_of_bombs(0, 11))
