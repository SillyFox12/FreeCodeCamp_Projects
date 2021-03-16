#Import necessary packages for project
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
#Name of project
root.title("Silly Fox's Tic Tac Toe Game")

#Amount of plays made 
count = 0
#Checks if play has clicked a button
clicked = True

#Button Click Detection Function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
    
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1

    else:
        messagebox.showerror("That position has already been taken.")




#Button Builder
b1 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
b2 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2))
b3 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3))

b4 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4))
b5 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5))
b6 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6))

b7 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7))
b8 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b8))
b9 = tk.Button(root, text = " ", font = ("Times", 24), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b9))


b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)

winning_combinations = ((b1["text"], b2["text"], b3["text"]), (b4["text"], b5["text"], b6["text"]), (b7["text"], b8["text"], b9["text"]), (b1["text"], b5["text"], b9["text"]), (b3["text"], b5["text"], b7["text"]), (b1["text"], b4["text"], b7["text"]),(b3["text"], b6["text"], b9["text"]))

root.mainloop()

