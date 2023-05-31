from hunian import Hunian
from tkinter import *
from PIL import ImageTk, Image

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, img_path, keterangan):
        super().__init__("Rumah", jml_penghuni, jml_kamar, img_path, keterangan)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik