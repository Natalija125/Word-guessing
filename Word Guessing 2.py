# word guessing
from tkinter import *
from itertools import chain

#import tkinter as tk #in that case we have to put tk. in front of built in methods, e.g. tk.Button(), tk.Frame() etc.

#layout
class WordGuessing(Frame): 
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Game Layout")
        self.root.geometry("1000x1000")
        self.root.resizable(True, True)

        #calling function that creates first frame
        self.CreateInterface1()

        #some important global variables for second and third frame
        self.remember_word = StringVar()
        self.remember_mistakes = StringVar()
        self.mistakes_counter = 0 #variable for counting mistakes
        self.letter_counter = 0 #variable for counting letters
        self.end_game = False #bool variable for game ending

        return
    
    #creating first interface
    def CreateInterface1(self):
        
        #creating first frame
        self.first_frame = Frame(bg = "#F5ECD5")
        self.first_frame.pack(expand = True, fill = BOTH)

        #redefining variables in case of playing again
        self.mistakes_counter = 0 #variable for counting mistakes
        self.letter_counter = 0 #variable for counting letters
        self.end_game = False #bool variable for game ending

        #rowspan and columnspan for grid
        for g in range(20):
            self.first_frame.rowconfigure(g, weight = 1)
            self.first_frame.columnconfigure(g, weight = 1)

        #button exit
        self.button_exit = Button(self.first_frame, command = self.CloseWindow, text = "X", font = ('Aharoni', 18, 'bold'), bg = "#F5B045")
        self.button_exit.grid(row = 0, column = 19, sticky = NE)
        
        #name of the game
        self.label_game_name = Label(self.first_frame, text = "Word guessing", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
        self.label_game_name.grid(row = 7, column = 9)

        #button start
        self.button_start = Button(self.first_frame, command = self.StartGame, text = "START", width = 20, font = ('Aharoni', 18, 'bold'), bg = "#F5B045")
        self.button_start.grid(row = 13, column = 9)

        return
    
    #close window function
    def CloseWindow(self):
        self.root.destroy()

    #start game from the first frame 
    def StartGame(self):

        self.first_frame.pack_forget() #removing old frame in purpose of creating new
        self.CreateInterface2() #calling function that creates second frame
        
        return
    
    #creating second interface
    def CreateInterface2(self):

        #creating second frame
        self.second_frame = Frame(bg = "#F5ECD5")
        self.second_frame.pack(expand = True, fill = BOTH)

        #rowspan and columnspan for grid
        for g in range(20):
            self.second_frame.rowconfigure(g, weight = 1)
            self.second_frame.columnconfigure(g, weight = 1)

        #button exit
        self.button_exit = Button(self.second_frame, command = self.CloseWindow, text = "X", font = ('Aharoni', 18, 'bold'), bg = "#F5B045")
        self.button_exit.grid(row = 0, column = 19, sticky = NE)

        #insert data
        self.label_insert_data = Label(self.second_frame, text = "Insert data", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
        self.label_insert_data.grid(row = 5, column = 9)     

        #label and entry for inserting a word
        self.label_word = Label(self.second_frame, text = "Insert a word", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
        self.label_word.grid(row = 9, column = 8)

        self.entry_word = Entry(self.second_frame, width = 40, font=('Aharoni', 12, 'bold'))
        self.entry_word.grid(row = 9, column = 10)

        #label and entry for inserting the maximum number of mistakes
        self.label_mistakes = Label(self.second_frame, text = "Insert a number of mistakes", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
        self.label_mistakes.grid(row = 11, column = 8)

        self.entry_mistakes = Entry(self.second_frame, width = 20 , font=('Aharoni', 12, 'bold'))
        self.entry_mistakes.grid(row = 11, column = 10)

        #button start
        self.button_start = Button(self.second_frame, command = self.StartGame2, text = "START", width = 20, font = ('Aharoni', 18, 'bold'), bg = "#F5B045")
        self.button_start.grid(row = 17, column = 9)

        return
    
    #start game from the second frame
    def StartGame2(self):

        self.second_frame.pack_forget() #removing old frame in purpose of creating new
        self.remember_word = self.entry_word.get() #grabbing word from the entry
        self.remember_mistakes = self.entry_mistakes.get() #grabbing maximum number of mistakes from the entry
        self.CreateInterface3() #calling function that creates third frame
        print(self.remember_word, self.remember_mistakes) #printing entry values in case of parameters check

        return

    #creating third interface
    def CreateInterface3(self):

        #creating third frame
        self.third_frame = Frame(bg = "#F5ECD5")
        self.third_frame.pack(expand = True, fill = BOTH)

        #rowspan and columnspan for grid
        for g in range(20):
            self.third_frame.rowconfigure(g, weight = 1)
            self.third_frame.columnconfigure(g, weight = 1)

        #button exit
        self.button_exit = Button(self.third_frame, command = self.CloseWindow, text = "X", font = ('Aharoni', 18, 'bold'), bg = "#F5B045")
        self.button_exit.grid(row = 0, column = 20, sticky = NE)

        #word
        self.remember_word_list = self.remember_word.split() #creating a list of words without spaces 
        self.extra_space_removed = " ".join(self.remember_word_list) #creating a new string without unwanted spaces
        self.remember_letters_list = list(self.extra_space_removed) #creating a list of letters, including spaces
        self.all_space_removed = "".join(self.remember_word_list) #creating a new string without any space
        self.remember_letters_list2 = list(self.all_space_removed) #creating a list of letters, without spaces
        print(self.remember_word_list) #printing s list of words in case of parameters check

        #calling function for creating (hidden) letters and placing them on grid
        self.place_elements()

        #creating an alphabet buttons, placing them on grid and creating commands
        self.letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", 
                        "f", "g", "h", "j", "k", "l" ,"z", "x", "c", "v", "b", "n", "m"]

        for i in range(len(self.letters)):

            if i <= 10:
                self.button_letters = Button(self.third_frame, text = self.letters[i], width = 2, font=('Aharoni', 12, 'bold'), bg = "#F5B045")
                self.button_letters.config(command = lambda let = self.letters[i], but = self.button_letters: self.read_button_letter(let, but))
                self.button_letters.grid(row = 10, column = i+5, padx = 5, pady = 5)

            elif i > 10 and i <= 21:
                self.button_letters = Button(self.third_frame, text = self.letters[i], width = 2, font=('Aharoni', 12, 'bold'), bg = "#F5B045")
                self.button_letters.config(command = lambda let = self.letters[i], but = self.button_letters: self.read_button_letter(let, but))
                self.button_letters.grid(row = 11, column = i-6, padx = 5, pady = 5)

            elif i > 21 and i <= 25:
                self.button_letters = Button(self.third_frame, text = self.letters[i], width = 2, font=('Aharoni', 12, 'bold'), bg = "#F5B045")
                self.button_letters.config(command = lambda let = self.letters[i], but = self.button_letters: self.read_button_letter(let, but))
                self.button_letters.grid(row = 12, column = i-17, padx = 5, pady = 5)

        #creating a "start over" button
        self.button_start_again = Button(self.third_frame, command = self.StartOver, text = "Start over", font = ('Aharoni', 18, 'bold'), bg = "#F5B045")
        self.button_start_again.grid(row = 19, column = 1, columnspan = 3)

        #calling mistakes function for printing and checking mistakes
        self.mistakes()

        return

    #creating function for grabbing letters from clicked alphabet buttons and placing them on the right position
    def read_button_letter(self, letter, button):
        print(letter)

        current_row = 5 #local variable for row tracking
        column_counter = -1 #local variable for column tracking
        mistake_appeared = False #local bool variable for spotting a mistake

        for w in self.remember_word_list:
            if len(w) + column_counter > 19: #because counter starts with -1 and there is 20 columns, starting from position 0 to 19
                current_row = 6
                column_counter = -1

            for l in range(len(w)):
                column_counter += 1
                print(column_counter)
                if letter in w and self.end_game == False:
                    if letter == w[l]: 
                        print(True)
                        self.revealed_letter = Label(self.third_frame, text = letter, font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
                        self.revealed_letter.grid(row = current_row, column = column_counter, padx = 5, pady = 5)
                        self.letter_counter += 1
                        button.config(bg = "green") #if the letter is correct make it green 
                
                if letter not in self.remember_letters_list and self.end_game == False:
                    mistake_appeared = True
                    button.config(bg = "red") #if the letter is wrong make it red
     
            if column_counter < 19:
                column_counter += 1

        if mistake_appeared == True:
            self.mistakes_counter += 1

        self.mistakes() #calling a function that tracks mistakes

    def mistakes(self): #creating function for mistakes

        mistakes_text = StringVar()

        if self.mistakes_counter == int(self.remember_mistakes): #if maximum number of mistakes is reached end game (you lose)
            self.end_game = True 
            self.place_elements()
            print("Game is over. You lost.")
            self.game_result = Label(self.third_frame, text = "You lost!", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
            self.game_result.grid(row = 16, column = 9, columnspan = 3)
        
        if self.end_game == False and self.letter_counter == len(self.remember_letters_list2): #if maximum number of mistakes is not reached end game (you won)
            self.end_game = True
            print("Game is over. You won.")
            self.game_result = Label(self.third_frame, text = "You won!", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
            self.game_result.grid(row = 16, column = 9, columnspan = 3)

        for i in range(17, 20):
            if i == 17:
                mistakes_text = str(self.mistakes_counter)   
            elif i == 18:
                mistakes_text = "/"
            else:
                mistakes_text = self.remember_mistakes
        
            self.label_mistakes = Label(self.third_frame, text = mistakes_text, font = ('Aharoni', 12, 'bold'), bg = "#F5ECD5")
            self.label_mistakes.grid(row = 19, column = i, padx = 5, pady = 5)

        return

    #creating function for (hidden) letters and placing them on grid
    def place_elements(self):
        
        current_row = 5 #local variable for row tracking
        column_counter = 0 #local variable for column tracking

        for w in self.remember_word_list:

            if len(w) + column_counter > 20:
                current_row = 6
                column_counter = 0

            for l in w:
                if self.end_game == False:
                    self.label_hidden_letter = Label(self.third_frame, text = "_", font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
                else:
                    self.label_hidden_letter = Label(self.third_frame, text = l, font = ('Aharoni', 18, 'bold'), bg = "#F5ECD5")
                self.label_hidden_letter.grid(row = current_row, column = column_counter, padx = 5, pady = 5)
                column_counter += 1
        
            if column_counter < 20:
                column_counter += 1

        return
    
    #creating start over function
    def StartOver(self):
        self.third_frame.pack_forget() #removing old frame in purpose of creating new
        self.CreateInterface1()

        return
                       
game = WordGuessing(Tk()) #making an object and starting a program
mainloop()
