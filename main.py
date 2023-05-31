from tkinter import *
from PIL import ImageTk, Image
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos

hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "assets/apartemen.jpg", "Apartemen berada di lantai 23."))
hunians.append(Rumah("Sekar MK", 5, 2, "assets/rumah2.jpg", None))
hunians.append(Indekos("Bp. Romi", "Cahya", "assets/indekos.png", None))
hunians.append(Rumah("Satria", 1, 4, "assets/rumah.jpg", None))

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    img = hunians[index].get_image()
    img_label = Label(d_frame, image=img)
    img_label.image = img
    img_label.grid(row=0, column=1)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    b_close = Button(d_frame, text="Close", command=top.destroy)
    b_close.grid(row=1, column=0)

def show_residents():
    root = Tk()
    root.title("Daftar Residen")
    frame = LabelFrame(root, text="Daftar Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)
    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)
    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    root.mainloop()

def landing_page():
    root = Tk()
    root.title("Praktikum DPBO Python")
    root.geometry("800x600")

    img = Image.open("assets/logo.png")
    img = img.resize((200, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(img)
    logo_label = Label(root, image=logo)
    logo_label.pack()

    welcome_label = Label(root, text="Welcome!", font=("Helvetica", 24))
    welcome_label.pack(pady=10)

    desc_label = Label(root, text="Please look around",
                        font=("Helvetica", 16), wraplength=400, justify="center")
    desc_label.pack(pady=20)

    b_residents = Button(root, text="Explore Residences", command=show_residents, font=("Helvetica", 16))
    b_residents.pack(pady=10)

    b_about = Button(root, text="About Developers", font=("Helvetica", 16))
    b_about.pack(pady=10)

    b_contact = Button(root, text="Contact Us", font=("Helvetica", 16))
    b_contact.pack(pady=10)

    footer_label = Label(root, text="© 2023 Ayurika")
    footer_label.pack(side="bottom", pady=10)

    root.mainloop()

landing_page()
