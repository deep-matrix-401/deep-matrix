from tkinter import *
from tkinter import messagebox
import pyttsx3
import sys
from tkinter.ttk import *
from PIL import ImageTk,Image
import uuid
import time





root = Tk()
root.title("Deep Matrix")
root.geometry('800x500')
root.iconbitmap('100766.ico')
root.configure(bg="#D4E6F1")



def talk():
    if my_entry.get() == "" : 
        messagebox.showinfo('Empty field' , 'Please Enter any text')
    else : 
        engine= pyttsx3.init()
        engine.say(my_entry.get())    
        engine.setProperty('rate', 100) 
        timestr = time.strftime("%Y%m%d-%H%M%S") 
        engine.save_to_file(my_entry.get(), f"{my_entry.get()[:10]}-{timestr}.mp3")
        engine.runAndWait()
        my_entry.delete(0,END)

style = Style()

my_entry=Entry(root, font = ("Helvetica" , 20)) 
my_entry.pack(pady=20)
my_button=Button(root , text="speak" ,command=talk , style = 'TButton')

my_button.pack(pady=20)
style.configure('TButton', font =
               ('calibri', 20, 'bold'),
                    borderwidth = '4')

style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])



root.mainloop()