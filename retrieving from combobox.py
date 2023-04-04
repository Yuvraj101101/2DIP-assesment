from tkinter import*
from tkinter import ttk
def retrieve():
    print(Combo.get())

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

subject_list = ["Maths","Calculus","Statistics","Physics","Chemistry"]
Combo = ttk.Combobox(frame, values = subject_list)
Combo.set("pick an option")
Combo.pack(padx=5 , pady=5)

Button= Button(frame, text="submit",command = retrieve)
Button.pack(padx = 5, pady = 5)

root.mainloop()
