import random
import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('600x600')

original_deck=[]
actual_deck=[]
random_deck=actual_deck
hand=[]
play=[]

objfile = open('objlist.txt')
all_the_lines = objfile.readlines()

for i in all_the_lines:
    original_deck.append(i)
       
def add_card_to_deck():
    actual_deck.append(choice.get())
    label2.configure(text=actual_deck)
    
def remove_card_from_deck():
    actual_deck.remove(choice.get())
    label2.configure(text=actual_deck)
def draw_hand():
    random.shuffle (random_deck)
    card = random.choice(random_deck)
    random_deck.remove(card)
    hand.append(card)
    hand_label.configure(text=hand)
            
#def put_card_in_play():
#
#def remove_card_from_hand():
#    
#def remove_card_from_play():
    
label1 = tk.Label(app, text = "Choose a card to add to/remove from deck")
label1.grid(column=0, row=0, columnspan=2)

choice = ttk.Combobox(app, values=original_deck)
choice.grid(columnspan=3, row=1)
choice.current(0)

button = tk.Button(text="add", font=40, command=add_card_to_deck)
button.grid(column=0,row=2)

button2 = tk.Button(text="remove", font=40, command=remove_card_from_deck)
button2.grid(column=1,row=2)

label2 = tk.Label(app, wraplength=500, text = "bleh")
label2.grid(column=0, row=4, columnspan=2)

button3 = tk.Button(text="draw hand", font=40, command=draw_hand)
button3.grid(column=0,row=5)

hand_label = tk.Label(app, wraplength=500, text="hand")
hand_label.grid(column=0, row=6, columnspan=2)
app.mainloop()
