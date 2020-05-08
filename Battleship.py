"""
Pitle: battleship.py
Author: Vickilee Thomas
Last modified: 5/7/2020

The purpose of this program is a game and serves as entertainment for those who are bored.
"""

import tkinter
import string
import random

boat1 = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
boat2 = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
boat3 = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
while boat1 == boat2:
    boat2 = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
    print(boat2)
while boat3 == boat1 or boat3 == boat2:
    boat3 = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
computer_boat = [boat1, boat2, boat3]
userboats = []
userhits = []
pchits = []
pcguesses = []


def user_boats():
    def set_boats():
        userboats.append(boat1entry.get())
        userboats.append(boat2entry.get())
        userboats.append(boat3entry.get())

    popup = tkinter.Tk()
    instructions = tkinter.Label(popup,text='Please choose a letter and number combination \nbetween a1 and e5, make sure letters are lowercase')
    instructions.grid(row=1)
    lable1 = tkinter.Label(popup, text='Enter Position of Boat 1: ')
    lable1.grid(row=2, column=1)
    boat1entry = tkinter.Entry(popup)
    boat1entry.grid(row=2, column=2)
    lable2 = tkinter.Label(popup, text='Enter Position of Boat 3: ')
    lable2.grid(row=3, column=1)
    boat2entry = tkinter.Entry(popup)
    boat2entry.grid(row=3, column=2)
    lable3 = tkinter.Label(popup, text='Enter Position of Boat 3: ')
    lable3.grid(row=4, column=1)
    boat3entry = tkinter.Entry(popup)
    boat3entry.grid(row=4, column=2)
    setboatsbutton = tkinter.Button(popup, text='set selection', command=set_boats)
    setboatsbutton.grid(row=5, column=1)
    close = tkinter.Button(popup, text='Close', command=popup.destroy)
    close.grid(row=5, column=2)


def pc_turn():
    guess = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
    while guess in pcguesses or guess in pchits:
        guess = random.choice(string.ascii_letters[0:3]) + str(random.randint(1, 5))
    if guess in userboats:
        pchits.append(guess)
        lable.config(text = 'PC hit at ' + str(guess))
        pchitlistlable.config(text = 'PC hits ' + str(pchits))
        if len(pchits) == 3:
            lable.config(text='PC Wins')
    else:
        lable.config(text='PC miss at ' + str(guess))
        pcguesses.append(guess)
    pcg.config(text='PC guess list' + str(pcguesses))

def choose_a1():
    print(computer_boat)
    if 'a1' in computer_boat:
        a1.config(text='HIT')
        a1['state'] = tkinter.DISABLED
        userhits.append('a1')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on A1')
        a1.config(text='x')
        a1['state'] = tkinter.DISABLED


def choose_a2():
    if 'a2' in computer_boat:
        a2.config(text='HIT')
        a2['state'] = tkinter.DISABLED
        userhits.append('a2')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on A2')
        a2.config(text='x')
        a2['state'] = tkinter.DISABLED


def choose_a3():
    if 'a3' in computer_boat:
        a3.config(text='HIT')
        a3['state'] = tkinter.DISABLED
        userhits.append('a3')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on A3')
        a3.config(text='x')
        a3['state'] = tkinter.DISABLED


def choose_a4():
    if 'a4' in computer_boat:
        a4.config(text='HIT')
        a4['state'] = tkinter.DISABLED
        userhits.append('a4')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on A4')
        a4.config(text='x')
        a4['state'] = tkinter.DISABLED


def choose_a5():
    if 'a5' in computer_boat:
        a5.config(text='HIT')
        a5['state'] = tkinter.DISABLED
        userhits.append('a5')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on A5')
        a5.config(text='x')
        a5['state'] = tkinter.DISABLED


def choose_b1():
    if 'b1' in computer_boat:
        b1.config(text='HIT')
        b1['state'] = tkinter.DISABLED
        userhits.append('B1')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on B1')
        b1.config(text='x')
        b1['state'] = tkinter.DISABLED


def choose_b2():
    if 'b2' in computer_boat:
        b2.config(text='HIT')
        b2['state'] = tkinter.DISABLED
        userhits.append('B2')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on B2')
        b2.config(text='x')
        b2['state'] = tkinter.DISABLED


def choose_b3():
    if 'b3' in computer_boat:
        b3.config(text='HIT')
        b3['state'] = tkinter.DISABLED
        userhits.append('B3')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on b3')
        b3.config(text='x')
        b3['state'] = tkinter.DISABLED


def choose_b4():
    if 'b4' in computer_boat:
        b4.config(text='HIT')
        b4['state'] = tkinter.DISABLED
        userhits.append('B4')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on b4')
        b4.config(text='x')
        b4['state'] = tkinter.DISABLED


def choose_b5():
    if 'b5' in computer_boat:
        b5.config(text='HIT')
        b5['state'] = tkinter.DISABLED
        userhits.append('b5')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on B5')
        b5.config(text='x')
        b5['state'] = tkinter.DISABLED


def choose_c1():
    if 'c1' in computer_boat:
        c1.config(text='HIT')
        c1['state'] = tkinter.DISABLED
        userhits.append('C1')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on C1')
        c1.config(text='x')
        c1['state'] = tkinter.DISABLED


def choose_c2():
    if 'c2' in computer_boat:
        c2.config(text='HIT')
        c2['state'] = tkinter.DISABLED
        userhits.append('C2')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on C2')
        c2.config(text='x')
        c2['state'] = tkinter.DISABLED


def choose_c3():
    if 'c3' in computer_boat:
        c3.config(text='HIT')
        c3['state'] = tkinter.DISABLED
        userhits.append('C3')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on C3')
        c3.config(text='x')
        c3['state'] = tkinter.DISABLED


def choose_c4():
    if 'c4' in computer_boat:
        c4.config(text='HIT')
        c4['state'] = tkinter.DISABLED
        userhits.append('c4')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on C4')
        c4.config(text='x')
        c4['state'] = tkinter.DISABLED


def choose_c5():
    if 'c5' in computer_boat:
        c5.config(text='HIT')
        c5['state'] = tkinter.DISABLED
        userhits.append('c5')
        lable.config(text='Hit')
        userhitlistlable.config(text = 'User hits' + str(userhits))
        print(len(userhits))
        if len(userhits) == 3:
            lable.config(text='User Wins!')
    else:
        lable.config(text='Miss on C5')
        c5.config(text='x')
        c5['state'] = tkinter.DISABLED


m = tkinter.Tk()
m.title('Battleship')
lable = tkinter.Label(m, text='No Selection Made')
lable.grid(row=15)
userhitlistlable = tkinter.Label(m,text = 'User hits' + str(userhits))
userhitlistlable.grid(row = 16)
pchitlistlable = tkinter.Label(m,text = 'PC hits ' + str(pchits))
pchitlistlable.grid(row = 17)
pcg = tkinter.Label(m,text='PC guess list' + str(pcguesses))
pcg.grid(row = 18)
userboatsss = tkinter.Label(m,text = str(userboats))

user = tkinter.Button(m, text='Enter boat positions', command=user_boats, width='25')
user.grid(row=0)
a1 = tkinter.Button(m, text='A1', command=choose_a1, width='5')
a1.grid(row=1, column=1)
a2 = tkinter.Button(m, text='A2', command=choose_a2, width='5')
a2.grid(row=1, column=2)
a3 = tkinter.Button(m, text='A3', command=choose_a3, width='5')
a3.grid(row=1, column=3)
a4 = tkinter.Button(m, text='A4', command=choose_a4, width='5')
a4.grid(row=1, column=4)
a5 = tkinter.Button(m, text='A5', command=choose_a5, width='5')
a5.grid(row=1, column=5)
b1 = tkinter.Button(m, text='B1', command=choose_b1, width='5')
b1.grid(row=2, column=1)
b2 = tkinter.Button(m, text='B2', command=choose_b2, width='5')
b2.grid(row=2, column=2)
b3 = tkinter.Button(m, text='B3', command=choose_b3, width='5')
b3.grid(row=2, column=3)
b4 = tkinter.Button(m, text='B4', command=choose_b4, width='5')
b4.grid(row=2, column=4)
b5 = tkinter.Button(m, text='B5', command=choose_b5, width='5')
b5.grid(row=2, column=5)
c1 = tkinter.Button(m, text='C1', command=choose_c1, width='5')
c1.grid(row=3, column=1)
c2 = tkinter.Button(m, text='C2', command=choose_c2, width='5')
c2.grid(row=3, column=2)
c3 = tkinter.Button(m, text='C3', command=choose_c3, width='5')
c3.grid(row=3, column=3)
c4 = tkinter.Button(m, text='C4', command=choose_c4, width='5')
c4.grid(row=3, column=4)
c5 = tkinter.Button(m, text='C5', command=choose_c5, width='5')
c5.grid(row=3, column=5)


pcturn = tkinter.Button(m,text = 'PC turn',command = pc_turn)
pcturn.grid(row=24)
exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
exit_button.grid(row=25)
m.mainloop()