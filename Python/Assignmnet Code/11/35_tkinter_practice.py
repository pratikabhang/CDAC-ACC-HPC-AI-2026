import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Tkinter Practice")
    window.geometry("300x150")
    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack(pady=20)
    button = tk.Button(window, text="Close", command=window.destroy)
    button.pack()
    window.mainloop()

create_window()