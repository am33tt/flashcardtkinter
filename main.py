import random
from tkinter import *
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#CEDEBD"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

rep = 0
lap = 0
a = None
b = ""
c = ""
chosen_num = []


def change1():
    global a, b, c, lap
    if lap % 2 == 0:
        a, b, c = mechanism()


def change():
    global rep, lap, a, b, c

    change1()

    if rep % 2 == 0:
        canvas2.itemconfig(image1, image=photo2)
        canvas2.itemconfig(text, text='French')
        canvas2.itemconfig(text2, text=f'{b}')
        rep += 1


    elif rep % 2 != 0:
        canvas2.itemconfig(image1, image=photo1)
        canvas2.itemconfig(text, text='English')
        canvas2.itemconfig(text2, text=f'{c}')
        rep += 1

    lap += 1


def countdown(sec, total_rep):
    global a
    chan = 0
    if sec > -2 and chan <= 1 and total_rep >= -1:
        if sec == -1:
            change()
            sec += 4
            chan += 1
        window.after(1000, countdown, sec - 1, total_rep - 1)
        canvas2.itemconfig(text3, text=f'⌚: {sec}')


def hehe():
    change()
    countdown(3, 6)


def right():
    global a
    chosen_num.append(a)
    try:
        with open ('chosen_num.txt', mode='a') as file:
            file.write( str(a) + '\n')
    except FileNotFoundError:
        with open('chosen_num.txt', mode='w') as file:
            file.write((str(a) + '\n'))

    print(chosen_num)
    hehe()
    return True


def wrong():
    hehe()
    return True

def reset():
    is_ok = messagebox.askokcancel(title='Careful', message='The words you previously marked as "Remembered" will be '
                                                            'shown again wih Flash Card.')
    if is_ok:
        with open('chosen_num.txt', mode='w') as file:
            pass

label = Label(text='Language Flash Card', font=('Oswald', 20, 'bold'), bg=BACKGROUND_COLOR)
label.grid(row=0, column=0, columnspan=2)

canvas2 = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
photo1 = PhotoImage(file='images/card_back.png')
photo2 = PhotoImage(file='images/card_front.png')
image1 = canvas2.create_image(400, 263, image=photo1)
canvas2.grid(pady=25, row=2, column=0, columnspan=2, rowspan=2)

text = canvas2.create_text(400, 120, text='Language: French', font=('Arial', 25, 'italic'), fill='black')
text2 = canvas2.create_text(405, 230, text='Welcome/Bienvenue', font=('Arial', 50, 'bold'), fill='black')
text3 = canvas2.create_text(400, 380, text='⌚', font=('Arial', 20, 'bold'), fill='black')

button1 = Button(text='✔', font=('arial', 20, "bold"), command=right)
button1.grid(row=4, column=0)

button2 = Button(text='❌', font=('arial', 20, "bold"), command=wrong)
button2.grid(row=4, column=1)

button3 = Button(text='Start', font=('arial', 10, "bold"), command=hehe)
button3.grid(row=5, column=0, columnspan=2, pady=30)

button4 = Button(text='Reset', font=('arial', 10, "bold"), command=reset)
button4.grid(row=6, column=0, columnspan=2, pady=5)

file = pandas.read_csv('data/french_words.csv')

for index in file:
    new_dictionary = {row['French']: row['English'] for (num, row) in file.iterrows()}
keys = []
values = []
for key in new_dictionary:
    keys.append(key)
    value = new_dictionary[key]
    values.append(value)


def mechanism():
    global chosen
    global chosen_num
    random_num = random.randint(1, 100)
    try:
        with open('chosen_num.txt', mode='r') as file:
            data = file.readlines()
    except FileNotFoundError:
        with open('chosen_num.txt', mode='w') as file:
            data = file.readlines()
    finally:
        if random_num in chosen_num and data:
            random_num = random.randint(1, 100)

    random_key = keys[random_num]
    random_value = values[random_num]

    return random_num, random_key, random_value


window.mainloop()
