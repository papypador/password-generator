import string
from random import randint ,choice
from tkinter import *


def generate_password ():
    password_max = 12
    password_min = 8
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(choice(all_chars)for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#créere la premiere fenetre

window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.minsize(720, 480)
window.maxsize(1080, 720)
window.iconbitmap("picture/iceberg.ico")
window.config(background='#2B2D42')

#crer frame principale
frame = Frame(window, bg='#2B2D42')

# creation d'image
width = 300
height = 300
image = PhotoImage(file="picture/connexion.png").zoom(19).subsample(32)
canvas = Canvas(window, width=width, height=height, bg='#2B2D42', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)
canvas.pack()

#crer une sous boite
right_frame = Frame(frame, bg='#2B2D42')


#creer titre
label_title = Label(right_frame, text="Mot de passe", font=("Arial", 20), bg='#2B2D42', fg='white')
label_title.pack()

#crer un input/entree/champ
password_entry = Entry(right_frame, font=("Arial", 20), bg='#2B2D42', fg='white')
password_entry.pack()

#creer un boutton
generator_password_button = Button(right_frame, text="Generate", font=("Arial", 20), bg='#2B2D42', fg='white', command=generate_password)
generator_password_button.pack(fill=X)

# on place la sous boite de la frame a droite
right_frame.grid(row=0, column=1, sticky=W)

#afficher frame
frame.pack(expand=YES)

#creation d'une bartre de menue
menu_bar =Menu(window)
#creer premier menu
file_menu =Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#configurer notre fenetre
window.config(menu=menu_bar)


window.mainloop()