import tkinter as tk
import random

class MineSweeper:
    def __init__(self, master, width, height, mines):
        self.master = master
        self.width = width
        self.height = height
        self.mines = mines
        self.tiles = []
        self.game_over = False
        self.create_board()
    
    def create_board(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                tile = tk.Button(self.master, width=2, height=1, command=lambda i=i, j=j: self.tile_clicked(i, j))
                tile.grid(row=i, column=j)
                row.append(tile)
            self.tiles.append(row)
        self.place_mines()
    
    def place_mines(self):
        mines = 0
        while mines < self.mines:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            if not self.tiles[y][x].mines:
                self.tiles[y][x].mine = True
                mines += 1
    
    def tile_clicked(self, row, col):
        if self.game_over:
            return
        tile = self.tiles[row][col]
        if tile.mine:
            tile.config(text='*', bg='red')
            self.game_over = True
            return
        count = self.count_mines(row, col)
        if count == 0:
            tile.config(bg='gray', relief=tk.SUNKEN)
            self.clear_surrounding_tiles(row, col)
        else:
            tile.config(text=count, relief=tk.SUNKEN)
    
    def count_mines(self, row, col):
        count = 0
        for i in range(max(row-1, 0), min(row+2, self.height)):
            for j in range(max(col-1, 0), min(col+2, self.width)):
                if self.tiles[i][j].mine:
                    count += 1
        return count
    
    def clear_surrounding_tiles(self, row, col):
        for i in range(max(row-1, 0), min(row+2, self.height)):
            for j in range(max(col-1, 0), min(col+2, self.width)):
                if self.tiles[i][j]['relief'] == tk.RAISED:
                    self.tile_clicked(i, j)

root = tk.Tk()
root.title('Mine Sweeper')
game = MineSweeper(root, 10, 10, 10)
root.mainloop()
