import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title('Frames and parenting')

test_frame = ttk.Frame(window, width = 150, height = 200, borderwidth = 10, relief = tk.GROOVE)
# normally, frame size is adjusted to its content
# this can be prevented with:
test_frame.pack_propagate(False)
test_frame.pack()

# parenting
label = ttk.Label(test_frame, text = 'label in frame')
label.pack()

button1 = ttk.Button(test_frame, text = 'this is a button')
button1.pack()

window.mainloop()