import math
import random
import tkinter as tk

def entry_action(text):
    current_text = labeldisplay.cget("text")
    labeldisplay.config(text=current_text + str(text))

def calc_action():
    text = labeldisplay.cget("text")
    if text == "":
        return
    if "** (1 /" in text:
        text += ")"
    try:
        result = eval(text)
    except ZeroDivisionError:
        result = "Durch 0 teilen nicht erlaubt!"
    finally:
        labeldisplay.config(text=str(result))

def bin_button_action():
    try:
        result = bin(int(labeldisplay.cget("text"))).lstrip("0b")
    except ValueError:
        result = "Ganze Zahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def oct_button_action():
    try:
        result = oct(int(labeldisplay.cget("text"))).lstrip("0o")
    except ValueError:
        result = "Ganze Zahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def hex_button_action():
    try:
        result = hex(int(labeldisplay.cget("text"))).lstrip("0x")
    except ValueError:
        result = "Ganze Zahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def bin_dec_button_action():
    try:
        result = int(labeldisplay.cget("text"), 2)
    except ValueError:
        result = "Binärzahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def oct_dec_button_action():
    try:
        result = int(labeldisplay.cget("text"), 8)
    except ValueError:
        result = "Ganze Zahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def hex_dec_button_action():
    try:
        result = int(labeldisplay.cget("text"), 16)
    except ValueError:
        result = "Ganze Zahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def square_button_action():
    zahl = labeldisplay.cget("text")
    if zahl == "":
        return
    else:
        result = int(zahl) ** 2
    labeldisplay.config(text=str(result))

def squareroot_button_action():
    zahl = labeldisplay.cget("text")
    if zahl == "":
        return
    elif int(zahl) < 0:
        result = "Ungültige Eingabe!"
    else:
        result = int(zahl) ** (1/2)
    labeldisplay.config(text=str(result))

def fact_button_action():
    try:
        result = math.factorial(int(labeldisplay.cget("text")))
    except ValueError:
        result = "Ganze Zahl benötigt!"
    finally:
        labeldisplay.config(text=str(result))

def lotto_button_action():
    labeldisplay.config(text=(sorted(random.sample(range(1, 50), k=6))))

def cel_fah_button_action():
    zahl = labeldisplay.cget("text")
    if zahl == "":
        return
    else:
        result = round(int(zahl) * 1.8 + 32)
    labeldisplay.config(text=str(result))

def fah_cel_button_action():
    zahl = labeldisplay.cget("text")
    if zahl == "":
        return
    else:
        result = round((int(zahl) - 32) * 5/9)
    labeldisplay.config(text=str(result))

def clear_button_action():
    labeldisplay.config(text="")


root = tk.Tk()
root.title("Taschenrechner")

root.configure(bg="black")

root.resizable(width=True,height=True)

# Frame für das Labeldisplay
frame_display = tk.Frame(root, bg="black")
frame_display.grid(column=0, row=0, padx='5', pady='5', sticky="w")

# Label + C + Quit im eigenen Frame
labeldisplay = tk.Label(frame_display, bg='white', width='20', text='')
labeldisplay.grid(column=0, row=0, padx='5', pady='5')

clear_button = tk.Button(frame_display, text="C", command=clear_button_action).grid(column=1, row=0, padx='5', pady='5', sticky="e")
quit_button = tk.Button(frame_display, text="Quit", command=root.destroy).grid(column=2, row=0, padx='5', pady='5', sticky="w")


# Buttons in einem anderen Teil des Grids
button_frame = tk.Frame(root, bg="black")
button_frame.grid(column=0, row=1, padx='5', pady='5', sticky="w")

button =[]
for i in range(10):
    button.append(i)

button[7] = tk.Button(button_frame, text="7", command= lambda: entry_action("7"), width=2, height=1).grid(column=0, row=0, padx='5', pady='5')
button[8] = tk.Button(button_frame, text="8", command= lambda: entry_action("8"), width=2, height=1).grid(column=1, row=0, padx='5', pady='5')
button[9] = tk.Button(button_frame, text="9", command= lambda: entry_action("9"), width=2, height=1).grid(column=2, row=0, padx='5', pady='5')
button[4] = tk.Button(button_frame, text="4", command= lambda: entry_action("4"), width=2, height=1).grid(column=0, row=1, padx='5', pady='5')
button[5] = tk.Button(button_frame, text="5", command= lambda: entry_action("5"), width=2, height=1).grid(column=1, row=1, padx='5', pady='5')
button[6] = tk.Button(button_frame, text="6", command= lambda: entry_action("6"), width=2, height=1).grid(column=2, row=1, padx='5', pady='5')
button[1] = tk.Button(button_frame, text="1", command= lambda: entry_action("1"), width=2, height=1).grid(column=0, row=2, padx='5', pady='5')
button[2] = tk.Button(button_frame, text="2", command= lambda: entry_action("2"), width=2, height=1).grid(column=1, row=2, padx='5', pady='5')
button[3] = tk.Button(button_frame, text="3", command= lambda: entry_action("3"), width=2, height=1).grid(column=2, row=2, padx='5', pady='5')
button[0] = tk.Button(button_frame, text="0", command= lambda: entry_action("0"), width=2, height=1).grid(column=1, row=3, padx='5', pady='5')

decpoint_button = tk.Button(button_frame, text=".", command= lambda: entry_action("."), width=2, height=1).grid(column=2, row=3, padx='5', pady='5')

bracket_open_button = tk.Button(button_frame, bg="#99cc00", text="(", command= lambda: entry_action("("), width=2, height=1).grid(column=3, row=0, padx='5', pady='5')
bracket_open_button = tk.Button(button_frame, bg="#99cc00", text=")", command= lambda: entry_action(")"), width=2, height=1).grid(column=4, row=0, padx='5', pady='5')

plus_button = tk.Button(button_frame, bg="yellow", text="+", command=lambda: entry_action("+"), width=2, height=1).grid(column=3, row=1, padx='5', pady='5')
minus_button = tk.Button(button_frame, bg="yellow", text="-", command=lambda: entry_action("-"), width=2, height=1).grid(column=3, row=2, padx='5', pady='5')
mult_button = tk.Button(button_frame, bg="yellow", text="*", command=lambda: entry_action("*"), width=2, height=1).grid(column=3, row=3, padx='5', pady='5')
div_button = tk.Button(button_frame, bg="yellow", text=":", command=lambda: entry_action("/"), width=2, height=1).grid(column=4, row=1, padx='5', pady='5')
modulo_button = tk.Button(button_frame, bg="yellow", text="%", command=lambda: entry_action("%"), width=2, height=1).grid(column=4, row=2, padx='5', pady='5')
pot_button = tk.Button(button_frame, bg="#cc99ff", text="x\u02B8", command=lambda: entry_action("**"), width=2, height=1).grid(column=5, row=1, padx='5', pady='5')
root_button = tk.Button(button_frame, bg="#cc99ff", text="\u02B8\u221Ax", command=lambda: entry_action("** (1 /"), width=2, height=1).grid(column=5, row=2, padx='5', pady='5')

bin_button = tk.Button(button_frame, bg="green", text="bin", command=bin_button_action, width=2, height=1).grid(column=0, row=5, padx='5', pady='5')
oct_button = tk.Button(button_frame, bg="green", text="oct", command=oct_button_action, width=2, height=1).grid(column=1, row=5, padx='5', pady='5')
hex_button = tk.Button(button_frame, bg="green", text="hex", command=hex_button_action, width=2, height=1).grid(column=2, row=5, padx='5', pady='5')

bin_dec_button = tk.Button(button_frame, bg="green", text="b>d", command=bin_dec_button_action, width=2, height=1).grid(column=3, row=5, padx='5', pady='5')
oct_dec_button = tk.Button(button_frame, bg="green", text="o>d", command=oct_dec_button_action, width=2, height=1).grid(column=4, row=5, padx='5', pady='5')
hex_dec_button = tk.Button(button_frame, bg="green", text="h>d", command=hex_dec_button_action, width=2, height=1).grid(column=5, row=5, padx='5', pady='5')


square_button = tk.Button(button_frame, bg="#cc99ff", text="x\u00B2", command=square_button_action, width=2, height=1).grid(column=6, row=1, padx='5', pady='5')
squareroot_button = tk.Button(button_frame, bg="#cc99ff", text="\u221A", command=squareroot_button_action, width=2, height=1).grid(column=6, row=2, padx='5', pady='5')
fact_button = tk.Button(button_frame, bg="#cc99ff", text="n!", command=fact_button_action, width=2, height=1).grid(column=5, row=0, padx='5', pady='5')

lotto_button = tk.Button(button_frame, bg="orange", text="Lot", command=lotto_button_action, width=2, height=1).grid(column=6, row=0, padx='5', pady='5')

cel_fah_button = tk.Button(button_frame, bg="red", text="C>F", command=cel_fah_button_action, width=2, height=1).grid(column=5, row=3, padx='5', pady='5')
fah_cel_button = tk.Button(button_frame, bg="red", text="F>C", command=fah_cel_button_action, width=2, height=1).grid(column=6, row=3, padx='5', pady='5')

button_a = tk.Button(button_frame, text="A", command= lambda: entry_action("a"), width=2, height=1).grid(column=0, row=4, padx='5', pady='5')
button_b = tk.Button(button_frame, text="B", command= lambda: entry_action("b"), width=2, height=1).grid(column=1, row=4, padx='5', pady='5')
button_c = tk.Button(button_frame, text="C", command= lambda: entry_action("c"), width=2, height=1).grid(column=2, row=4, padx='5', pady='5')
button_d = tk.Button(button_frame, text="D", command= lambda: entry_action("d"), width=2, height=1).grid(column=3, row=4, padx='5', pady='5')
button_e = tk.Button(button_frame, text="E", command= lambda: entry_action("e"), width=2, height=1).grid(column=4, row=4, padx='5', pady='5')
button_f = tk.Button(button_frame, text="F", command= lambda: entry_action("f"), width=2, height=1).grid(column=5, row=4, padx='5', pady='5')


equals_button = tk.Button(button_frame, bg="turquoise", text="=", command=calc_action, width=2, height=1).grid(column=4, row=3, padx='5', pady='5')

root.mainloop()