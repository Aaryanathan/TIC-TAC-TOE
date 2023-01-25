from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("Tic Tac Toe")
root.configure(bg="black")
Label(root, text="player1 : X", font="times 15", fg="light green", bg="black").grid(row=0, column=1)
Label(root, text="player2 : O", font="times 15", fg="cyan", bg="black").grid(row=1, column=1)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ''
count = 0
panels = ['panel']*10

def win(panels, sign):
    return ((panels[1] == panels[2] == panels[3] == sign)
            or (panels[1] == panels[4] == panels[7] == sign)
            or (panels[1] == panels[5] == panels[9] == sign)
            or (panels[2] == panels[5] == panels[8] == sign)
            or (panels[3] == panels[6] == panels[9] == sign)
            or (panels[3] == panels[5] == panels[7] == sign)
            or (panels[4] == panels[5] == panels[6] == sign)
            or (panels[7] == panels[8] == panels[9] == sign))

def checker(digit):
    global count, mark, digits
    if digit == 1 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button1.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 2 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button2.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 3 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button3.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 4 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button4.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 5 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button5.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 6 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button6.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 7 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button7.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 8 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button8.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 9 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button9.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')
    if digit == 1 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        button1.config(text = mark)
        count = count + 1
        sign = mark    
        if win(panels, sign) and sign == "X":
            msg.showinfo('Result: ', 'Player 1 wins')
        if win(panels, sign) and sign == "O":
            msg.showinfo('Result: ', 'Player 2 wins')

button1 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(1), fg='white', bg='black')
button1.grid(row=2, column=1)
button2 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(2), fg='white', bg='black')
button2.grid(row=3, column=1)
button3 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(3), fg='white', bg='black')
button3.grid(row=4, column=1)
button4 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(4), fg='white', bg='black')
button4.grid(row=2, column=2)
button5 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(5), fg='white', bg='black')
button5.grid(row=3, column=2)
button6 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(6), fg='white', bg='black')
button6.grid(row=4, column=2)
button7 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(7), fg='white', bg='black')
button7.grid(row=2, column=3)
button8 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(8), fg='white', bg='black')
button8.grid(row=3, column=3)
button9 = Button(root, width=15, font=('times 16 bold'), height=7, command=lambda:checker(9), fg='white', bg='black')
button9.grid(row=4, column=3)

root.mainloop()