from hunian import Hunian
from tkinter import *
from PIL import ImageTk, Image

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, img_path, keterangan):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, img_path, keterangan)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik