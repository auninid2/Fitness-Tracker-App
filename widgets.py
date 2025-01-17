# GUI tasarımında her şey widgetlardan oluşuyor. Programın yaptığı bu widgetları farklı yerlere koyup interaktif hale getirmek 
# Bunun için ilk olarak bir widget oluştuyorsun, örneğin tk.Text ya da ttk.Label. Sonrasında .pack gibi metodlarla ekrana koyuyorsun.
# Örnek widgetlar: tk.Text, ttk.Entry, ttk.Label, ttk. Button

import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')
    
def say_hello():
    print('hello')

# create a window
window = tk.Tk()
window.title('Windows and Widgets')
window.geometry('700x500')

# ttk label
label = ttk.Label(master = window, text = 'this is a test')
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# label
label = ttk.Label(master = window, text = 'my label')
label.pack()

# button
button_test = ttk.Button(master = window, text = 'exercise button', command = lambda: print('hello'))
button_test.pack()

# run
window.mainloop()