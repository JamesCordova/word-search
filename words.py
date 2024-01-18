# Word search game:
# We are gonna create a word search game with pygame or tkinter
# so for that we need to create a table of the words where should include 
# the hidden words.

# The game should have the following:
# - Table of words
# - Words to find
# - Timer
# - Score
# - Hints
# - Menu

# The game should start with a menu where you can choose the difficulty
# and the words to find, then the game should start with the timer
# and the score, the words to find should be displayed in the screen
# and the table of words should be displayed with the hidden words
# and the rest of the table should be filled with random letters.
# The words to find should be displayed in the screen and when you
# find a word it should be displayed in the screen with a different
# color and the score should be increased.

import tkinter as tk
import ctypes
import random
import customtkinter as ctk
import settings as cf
from PIL import ImageTk

class GameWordSearch(ctk.CTk):
    def __init__(self, title_game = cf.GAME_NAME):
        super().__init__()
        self.title(title_game)
        self.color_ui = (cf.BG_COLOR_DARK, cf.BG_COLOR_LIGHT)

        self.configure(
            background = self.color_ui
        )

        # setting header
        
        self.game = GameFrame(self)

        self.game.pack(
            side = tk.BOTTOM,
            expand = True,
            padx = 20,
            pady = 15,
            fill = "x"
        )

        self.header = GameHeaderFrame(
            master = self,
            data = {"nivel": 10}
        )
        self.header.pack(
            side = tk.BOTTOM,
            expand = True,
            padx = 20,
            pady = 15,
            fill = "x"
        )

        # setting the icon
        try:
            icon_ctk = ImageTk.PhotoImage(file = cf.ICON_IMAGE)
            self.wm_iconbitmap()
            self.iconphoto(False, icon_ctk)
            self.myappid = "word.search.game.1"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.myappid)
        except:
            pass

        self.geometry("810x700")
        self.maxsize(810, 700)

    def run(self):
        self.mainloop()

class GameHeaderFrame(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(
            master = master,
            fg_color = "transparent"
        )

        self.title = ctk.CTkLabel(
            master = self,
            text = "Word Search",
            fg_color = "transparent",
            bg_color = "transparent",
            font = ("Arial", 20)
        )

        self.title.pack()

class GameFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master = master,
            fg_color = "transparent"
        )
        self.words = ["PRUEBA", "PARA", "DESARROLLO", "EJEMPLO", "NOVEDAD", "PALABRA", "NUEVA", "CUESTION", "PROBLEMA", "SITUACION"]
        self.orientations = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        self.columnconfigure(0, weight = 3)
        self.columnconfigure(1, weight = 1)

        self.create_table()
        self.render_table()

        self.word_grid_frame = WordGridFrame(self, self.grid, self.words)

        self.word_grid_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.word_list_frame = ListWordsFrame(self, self.words)

        self.word_grid_frame.bind("<<FoundWord>>", self.hide_question)

        self.word_list_frame.grid(row = 0, column =1)

    def create_table(self):
        size = 20
        self.grid = [['_' for _ in range(size)] for __ in range(size)]

        for word in self.words:
            word_length = len(word)

            is_placed = False

            while not is_placed:
                orientation = random.choice(self.orientations)
                x_pos = random.randint(0, size - 1)
                y_pos = random.randint(0, size - 1)
                
                end_x = x_pos + word_length * orientation[0]
                end_y = y_pos + word_length * orientation[1]

                if end_x < 0 or end_x >= size:
                    continue
                if end_y < 0 or end_y >= size:
                    continue

                is_failed = False

                # We run through the characters of the word by a index and 
                # we replace with it if is possible
                for i in range(word_length):
                    current_x = x_pos + i * orientation[0]
                    current_y = y_pos + i * orientation[1]
                    if self.grid[current_y][current_x] != '_' and self.grid[current_y][current_x] != word[i]:
                        is_failed = True
                        break;
                        
                # If we failed putting in the grid then we should do this again
                if is_failed:
                    continue
                else:
                    for i in range(word_length):
                        current_x = x_pos + i * orientation[0]
                        current_y = y_pos + i * orientation[1]
                        self.grid[current_y][current_x] = word[i]

                    is_placed = True

        self.replace_blanks()
        print_grid(self.grid)

    def replace_blanks(self):
        size = len(self.grid)
        for i in range(size):
            for j in range(size):
                if self.grid[i][j] == '_':
                    self.grid[i][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def render_table(self):
        pass

    def hide_question(self, event):
        print("Event done")
        word = self.word_grid_frame.last_word
        self.word_list_frame.hide_question(self.words.index(word))

class WordGridFrame(ctk.CTkFrame):
    def __init__(self, master, plain_grid = [], word_list = []):
        super().__init__(
            master = master,
            fg_color = "transparent"
        )
        self.plain_grid = plain_grid
        self.word_list = word_list
        self.current_selection = {
            "Positions": [],
            "Direction": [0, 0],
            "Word": ""
        }
        self.set_grid()
        # self.render_grid()
    pass

    def set_grid(self):
        rows = len(self.plain_grid)
        cols = len(self.plain_grid[0])
        self.buttons = [[0 for _ in range(rows)] for __ in range(cols)]
        for y in range(rows):
            for x in range(cols):
                text = self.plain_grid[y][x]
                self.buttons[y][x] = ctk.CTkButton(
                    master = self,
                    text = text,
                    width = 3,
                    height = 1,
                    corner_radius = 0,
                    fg_color = "transparent",
                    hover_color = (cf.HOVER_COLOR_LIGHT, cf.HOVER_COLOR_DARK),
                    command = lambda x=x, y=y, t= text: self.button_pressing(x, y, t)
                )
                self.buttons[y][x].grid(row = y, column = x, sticky = "nsew")
    def button_pressing(self, x, y, text):

        self.buttons[y][x].configure(
            bg_color = cf.SELECT_COLOR_LIGHT,
            hover_color = (cf.SELECT_COLOR_LIGHT, cf.SELECT_COLOR_DARK)
        )

        if not self.is_adjacent(x,y) or not self.is_same_direction(x,y):
            self.recolor_selection(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK)
            self.current_selection["Word"] = ""
            self.current_selection["Positions"] = []

        self.current_selection["Word"] += text
        self.current_selection.get("Positions").append([x, y])
        if self.current_selection["Word"] in self.word_list:
            print(self.current_selection["Word"])
            self.last_word = self.current_selection["Word"]
            self._canvas.event_generate("<<FoundWord>>")
            self.recolor_selection(cf.SUCCESS_COLOR_LIGHT, cf.SUCCESS_COLOR_DARK)
            self.current_selection["Word"] = ""
            self.current_selection["Positions"] = []

    def get_direction(self, first_xy, second_xy):
        x, y = second_xy[0] - first_xy[0], second_xy[1] - first_xy[1]
        return [x,y]
    
    def is_adjacent(self, cur_x, cur_y):
        if len(self.current_selection.get("Positions")) == 0:
            return True
        ls_x, ls_y = self.current_selection.get("Positions")[-1]
        if abs(cur_x - ls_x) > 1:
            return False
        if abs(cur_y - ls_y) > 1:
            return False
        return True
    
    def recolor_selection(self, light_color, dark_color):
        for position in self.current_selection.get("Positions"):
            x, y = position
            self.buttons[y][x].configure(
                bg_color = (light_color, dark_color),
            )

    def is_same_direction(self, x, y):
        if len(self.current_selection.get("Positions")) == 1 or len(self.current_selection.get("Positions")) == 0:
            self.current_selection["Direction"] = [0, 0]
            return True
        last_xy = self.current_selection.get("Positions")[-1]
        direction = self.get_direction(last_xy, [x, y])
        
        if len(self.current_selection.get("Positions")) == 2:
            first_xy = self.current_selection.get("Positions")[0]
            second_xy = self.current_selection.get("Positions")[1]
            x_direction, y_direction = self.get_direction(first_xy, second_xy)
            self.current_selection["Direction"] = [x_direction, y_direction]

        return self.current_selection["Direction"] == direction

class ListWordsFrame(ctk.CTkFrame):
    def __init__(self, master, word_list = []):
        super().__init__(
            master = master,
            fg_color = "transparent"
        )
        self.words = word_list
        self.word_amount = len(self.words)
        self.label_words = [0 for i in range(self.word_amount)]
        self.set_list()

    def set_list(self):
        for i in range(self.word_amount):
            self.label_words[i] = ctk.CTkLabel(
                master = self,
                text = self.words[i],
                fg_color = "transparent",
                bg_color = "transparent"
            )
            self.label_words[i].pack()

    def hide_question(self, index):
        self.label_words[index].configure(
            fg_color = cf.SUCCESS_COLOR_LIGHT
        )
    pass

        

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def run_game():
    game = GameWordSearch()
    game.run()

if __name__ == "__main__":
    run_game()