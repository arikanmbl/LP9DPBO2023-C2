from tkinter import *
from PIL import ImageTk, Image

class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, img_path = None, keterangan = None):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.img_path = img_path
        self.keterangan = keterangan

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_keterangan(self):
        return self.keterangan

    def get_summary(self):
        summary = "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang, dengan jumlah kamar " + str(self.jml_kamar) + "."
        if self.keterangan is not None:
            summary += "\nInformasi tambahan: " + self.keterangan
        summary += "\nDokumen: " + self.get_dokumen() + "."
        return summary

    def get_image(self):
        img = Image.open(self.img_path)
        img = img.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)