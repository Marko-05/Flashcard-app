
import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    words = pandas.read_csv("data/words_to_learn.csv")
    words = words.to_dict(orient="records")
except FileNotFoundError:
    words = pandas.words = pandas.read_csv("data/french_words.csv")
    words = words.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    words = []

current_word = {}


def next_card(delete_word=False):

    global current_word,flip_timer
    window.after_cancel(flip_timer)

    if delete_word:
        words.remove(current_word)
        new_data=pandas.DataFrame(data=words)
        new_data.to_csv("data/words_to_learn.csv",index=False)

    if len(words) > 0:
        selected = random.choice(words)
        current_word = selected
        canvas.itemconfig(background_img, image=card_front)
        canvas.itemconfig(language_text, text="French",fill="black")
        canvas.itemconfig(word_text,text=selected["French"], fill="black")
        flip_timer = window.after(3000,flip_card)

    else:
        canvas.itemconfig(background_img, image=card_front)
        canvas.delete(language_text)
        canvas.itemconfig(word_text, font = ("Ariel",22,"bold"),text="You have learned all of the words.\n\t  Good Job!",fill="black")
        canvas.create_text(400,400,font=("Ariel",18,"bold"),text="To learn new words, add them to the words_to_learn.csv file.\n\tThe file should be located in the data folder.")
        wrong_button.destroy()
        right_button.destroy()

def flip_card():
    global current_word
    canvas.itemconfig(background_img, image = card_back)
    canvas.itemconfig(language_text,text="English",fill = "white")
    canvas.itemconfig(word_text,text = current_word["English"],fill="white")

window = Tk()
window.config(pady=50,padx=50,background=BACKGROUND_COLOR)
window.title("Flashy")


card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,columnspan=2,row=0)
background_img = canvas.create_image(400,263,image=card_front)

language_text = canvas.create_text(400,150,font=("Ariel",40,"italic"),text="Title")
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="Word")


right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0,borderwidth=0,anchor="center",command=lambda: next_card(delete_word=True))
right_button.grid(row=1,column=0)


wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong,highlightthickness=0,borderwidth=0,anchor="center",command=lambda: next_card(delete_word=False))
wrong_button.grid(row=1,column=1)

flip_timer = window.after(3000,flip_card)

next_card()

window.mainloop()
