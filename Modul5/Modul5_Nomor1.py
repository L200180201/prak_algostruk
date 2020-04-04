from Kegiatan_Modul5 import *

class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya.'
        return s

a0 = MhsTIF("Aldy", 175, "Sukoharjo", 290000)
a1 = MhsTIF("Wafiq", 178, "Rembang", 300000)
a2 = MhsTIF("Hanan", 170, "Sragen", 280000)
a3 = MhsTIF("Herlangga", 186, "Karanganyar", 250000)
a4 = MhsTIF("Fatwa", 176, "Boyolali", 310000)
a5 = MhsTIF("Yusuf", 169, "Karanganyar", 255000)
a6 = MhsTIF("Ghani", 185, "Boyolali", 320000)
a7 = MhsTIF("Kevin", 182, "Wonogiri", 270000)
a8 = MhsTIF("Azka", 181, "Karanganyar", 265000)
a9 = MhsTIF("Hanif", 201, "Semarang", 275000)
a10 = MhsTIF("Riyan", 180, "Sukoharjo", 265000)

Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

def urutkanNim(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
    insertionSort(NIM)
    return NIM
