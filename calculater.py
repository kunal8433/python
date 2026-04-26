
import tkinter as tk

# main window
root = tk.Tk()
root.title("KUNAL Calculator")
root.geometry("350x500")
root.resizable(False, False)

# entry box
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.pack(fill="x", padx=10, pady=10)

# function to click button
def click(value):
    entry.insert(tk.END, value)

# function to clear
def clear():
    entry.delete(0, tk.END)

# function to calculate
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# frame for buttons
frame = tk.Frame(root)
frame.pack()

buttons = [
    '2' , '3' , '4' , '5' , '6' , '7'
    '8', '9' , '0' , '-' , '*' , ' -'
    , '+' , '\\' , '@', '??' , " 23"
    , '45' , "54" , '56' , "55"
]

row = 0
col = 0

for btn in buttons:
    if btn == "=":
        b = tk.Button(frame, text=btn, width=10, height=2,
                      command=calculate)
    else:
        b = tk.Button(frame, text=btn, width=5, height=2,
                      command=lambda x=btn: click(x))
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# clear button
clear_btn = tk.Button(root, text="Clear", width=20, height=2, command=clear)
clear_btn.pack(pady=10)

root.mainloop()

print('kun l')
print()
print