from tkinter import Tk, Text, Button
value = ""
win = None

def return_value(text_box):
    global value
    value = text_box.get("1.0", "end-1c")
    if win is not None:
        win.destroy()

def make_textbox(width, height, default="", message="Set Step Title"):
    global win
    win=Tk()
    win.geometry(f"{width}x{height}")
    win.title(message)

    text_box=Text(win, width=50, height=1)
    text_box.pack()
    text_box.insert(1.0, default)

    # comment= Button(win, height=1, width=10, text="Enter", command=lambda: return_value(text_box))
    # comment.pack()
    
    win.attributes('-topmost',True)
    win.protocol("WM_DELETE_WINDOW", lambda: return_value(text_box))
    win.mainloop()
