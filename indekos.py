from hunian import Hunian
from tkinter import *
from PIL import ImageTk, Image

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, img_path, keterangan):
        super().__init__("Indekos", img_path=img_path)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos, pemilik: " + self.nama_pemilik + ", penghuni: " + self.nama_penghuni + ". \nDokumen: " + self.get_dokumen() + "."