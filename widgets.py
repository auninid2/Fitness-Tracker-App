# GUI tasarımında her şey widgetlardan oluşuyor. Programın yaptığı bu widgetları farklı yerlere koyup interaktif hale getirmek 
# Bunun için ilk olarak bir widget oluştuyorsun, örneğin tk.Text ya da ttk.Label. Sonrasında .pack gibi metodlarla ekrana koyuyorsun.
# Örnek widgetlar: tk.Text, ttk.Entry, ttk.Label, ttk. Button

import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Windows and Widgets')
# window.iconbitmap('example.iso')

# window.minsize(200, 100)
# window.maxsize(700, 600)
# window.resizeable(False, False)

# start window in the middle of the screen
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# tkinter variable
# widgets can be connected by assigning the same value to multiple widgets
string_var = tk.StringVar()

# change the value of a var
string_var.set('button pressed')

# label widget
label = ttk.Label(master = window, text = 'this is a label')
label.pack()

# entry widget
entry = ttk.Entry(window, textvariable = string_var)
entry.pack()

# text widget
text = tk.Text(window)
text.pack()

# button widget
button_test = ttk.Button(window, text = 'exercise button', command = lambda: print('hello'))
button_test.pack()

# all config options a widget has
print(label.configure()) 

# get the entry of a widget
entry_text = entry.get()

# widgets can be updated with config
label['text'] = entry_text
entry['state'] = 'disabled'

# events are binded to widgets
window.bind('<Alt-KeyPress-a>', lambda event: print('an event'))

# run
window.mainloop()