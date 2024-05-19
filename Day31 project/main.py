import csv
from tkinter import *
from tkinter import messagebox
import random
import pandas
from math import *

file = pandas.read_csv("data/JPwords - Sheet1.csv")
to_learn = file.to_dict(orient="records")
current_card_num = 0


def next_card():
    global current_card_num, flip_timer
    window.after_cancel(flip_timer)
    current_card_num = random.randrange(1, len(to_learn))
    canvas.itemconfig(card_title, text="Japanease", fill="black")
    canvas.itemconfig(card_word, text=to_learn[current_card_num]["JPWORD"], fill="black")
    canvas.itemconfig(jp_img, image=front_img)
    flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    canvas.itemconfig(jp_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=to_learn[current_card_num]["ENGWORD"], fill="white")


#UI_________________________________


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
jp_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3, rowspan=3)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 250, text="Word", font=("Ariel", 60, "bold"))
card_back = PhotoImage(file="images/card_back.png")


unknown_btn = PhotoImage(file="images/wrong.png")
uk_btn = Button(image=unknown_btn, highlightthickness=0)
uk_btn.grid(column=0, row=3)
known_btn = PhotoImage(file="images/right.png")
k_btn = Button(image=known_btn, highlightthickness=0, command=next_card)
k_btn.grid(column=2, row=3)

next_card()
window.mainloop()

