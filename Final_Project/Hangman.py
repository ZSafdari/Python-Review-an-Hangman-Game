# Final Project: Hangman Game

from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
from pygame import mixer


mixer.init()
mixer.music.load("Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Time Lapse.mp3")
mixer.music.play(-1)

win1 = Tk()
win1.title("Start!")
win1.geometry("640x480")
win1.resizable(False, False)

photo1 = PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\bg.png")
lb1 = Label(win1, image=photo1)
lb1.pack()

def openwindow():
    win1.destroy()
    top = Tk()
    f1 = Frame(top, height=220, width=220, bg="#FFD700")
    f1.place(x=10, y=10)
    f2 = Frame(top, height=250, width=220, bg="#FFD700")
    f2.place(x=400, y=190)
    f3 = Frame(top, height=630, width=530, bg="#FFD700")
    f3.place(x=18, y=340)
    top.title("Hangman")
    top.geometry("845x640")
    top.resizable(False, False)
    top.config(bg="#FFD700")

    word_list = ["CSHARP", "JAVASCRIPT", "PYTHON", "JAVA",
                 "DELFI", "REACT", "RUBY", "MATLAB", "SWIFT"]

    photos = [PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\1.png"),
              PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\2.png"),
              PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\3.png"),
              PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\4.png"),
              PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\5.png"),
              PhotoImage(file="Python Reveiw and Hangman Game\\Final_Project\\Hangman\\Images\\6.png")]

    def ExitWindow():
        answer1 = messagebox.askquestion("Oops! Game Over!", "Do you want to try again?", icon="warning")
        if answer1 == "yes":
            newGame()
        else:
            top.destroy()

    def PlayWindow():
        answer2 = messagebox.askquestion("Congrats! You won!", "Do you want to try again?", icon="info")
        if answer2 == "yes":
            newGame()
        else:
            top.destroy()

    def newGame():
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses = 0
        imgLabel.config(image=photos[0])
        the_word = random.choice(word_list)
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(" ".join("_" * len(the_word)))

    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses < 5:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    PlayWindow()
            else:
                numberOfGuesses += 1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses == 5:
                    ExitWindow()

    imgLabel = Label(f1)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    imgLabel.config(image=photos[0], width=250, height=250, bg="#FFD700")

    lblWord = StringVar()
    Label(f2, textvariable=lblWord, bg="#FFD700",
          font=("Fixedsys 17 bold")).grid(row=0, column=3, columnspan=6, padx=10)

    # Keyboard frame inside f3, packed for centering
    keyboard_frame = Frame(f3, bg="#FFD700")
    keyboard_frame.pack(pady=(20, 10))

    # Configure columns for even expansion (optional, but helps layout)
    for i in range(8):
        keyboard_frame.grid_columnconfigure(i, weight=1)

    # Letter buttons
    n = 0
    for c in ascii_uppercase:
        Button(keyboard_frame, text=c, command=lambda c=c: guess(c), font=("Fixedsys", 17, "bold"),
               bd=2, activebackground="green", width=4, bg="black", fg="#FFD700",
               relief="raised").grid(row=n // 8, column=n % 8, padx=3, pady=3, sticky="nsew")
        n += 1

    # New Game button below keyboard frame
    Button(f3, text="New Game", font=("Fixedsys", 15, "bold"), relief="raised", bd=4,
           activebackground="red", fg="black", bg="green", command=newGame, width=20).pack(pady=20)

    newGame()
    top.mainloop()


btn1 = Button(win1, text="Play", font="Fixedsys 12", bg="#7e7e7e", fg="black", command=openwindow)
btn1.config(activebackground="grey", activeforeground="white", relief="raised", bd=8)
btn1.place(height=50, width=100, x=420, y=280)

win1.mainloop()
