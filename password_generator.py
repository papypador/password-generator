import string
import os
from tkinter import *
from tkinter.messagebox import showinfo
from random import randint, choice

def generate_password():
    password_max = 24
    password_min = 12
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(choice(all_chars)for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    password = str(password)
    with open("last_password.txt", "a+") as file:
        file.write(password + "\n")
        file.close

def delete_save_password():
    if os.path.isfile("last_password.txt"):
        with open("last_password.txt") as file:
            os.remove("last_password.txt")
            showinfo("alert", "le fichier à été supprimé")
    else:
        showinfo("alert", "Il n'existe pas de sauvegarde")

window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.minsize(720, 480)
window.maxsize(1080, 720)
window.iconbitmap("iceberg.ico")
window.config(background='#2B2D42')
#window
frame = Frame(window, bg='#2B2D42')
#picture
width = 300
height = 300
image = PhotoImage(file="password.png").zoom(19).subsample(32)
canvas = Canvas(window, width=width, height=height, bg='#2B2D42', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)
canvas.pack()


right_frame = Frame(frame, bg='#2B2D42')
label_title = Label(right_frame, text="Mot de passe", font=("Arial", 20), bg='#2B2D42', fg='white')
label_title.pack()
password_entry = Entry(right_frame, font=("Arial", 20), bg='#2B2D42', fg='white')
password_entry.pack()
generator_password_button = Button(right_frame, text="Generate", font=("Arial", 20), bg='#2B2D42', fg='black', command=generate_password)
generator_password_button.pack(fill=X)
clear_password_button = Button(right_frame, text="clear sav", font=("Arial", 20), bg='#2B2D42', fg='black', command=delete_save_password)
clear_password_button.pack()
right_frame.grid(row=0, column=1, sticky=W)


frame.pack(expand=YES)


menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)


window.config(menu=menu_bar)
window.mainloop()
