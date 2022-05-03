from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Python Guides')
ws.geometry('300x100')

def askMe():
    res = messagebox.askquestion('askquestion', 'Do you like cats?')
    if res == 'yes':
        messagebox.showinfo('Response', 'You like Cats')
    elif res == 'no':
        messagebox.showinfo('Response', 'You must be a dog fan.')
    else:
        messagebox.showwarning('error', 'Something went wrong!')


Button(ws, text='Click here', padx=10, pady=5, command=askMe).pack(pady=20)

ws.mainloop()