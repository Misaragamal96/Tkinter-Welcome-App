from  tkinter import *

window = Tk()
window.title(" Misara Gamal")
window.geometry("400x300")
window.configure(bg="#ddd")
LabelE = Label(window, text="enter name :- ", font=("Arial" , 14))
LabelE.pack(pady=10)
name_entry = Entry(window , font=("Arial" , 14))
name_entry.pack(pady=10)
def show_message():
	name = name_entry.get()
	welcome_label.config(text=f"welcome، {name}!")
welcome_label = Label(window, text="Welcome message will appear here", font=("Arial", 16), fg="blue")
welcome_label.pack(pady=10)

button = Button(window, text=" welcome",font=("Arial" , 14), command=show_message)
button.pack(pady=10)
window.mainloop()