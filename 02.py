class nim(object):
    def __init__(self, nameInput, nimInput):
        self.name= nameInput
        self.nim = "2021" + nimInput
    def siapaAku(self):
        print("\nAku adalah {}".format(self.name))
    def sebutNim(self):
        print(self.nim)
        
class biodata(nim):
    def __init__(self, name, alamat, nimX):
        self.name= name
        self.alamat= alamat
        nim.__init__(self, name, nimX)
    def tanya_alamat(self):
        print("Aku tinggal di " + self.alamat)

namaI= input("Masukkan nama: ")
alamatI= input("Masukkan alamat: ")
nimI= input("Masukkan NIM: ")

mahasiswa1= biodata(namaI, alamatI, nimI)

mahasiswa1.siapaAku()
mahasiswa1.tanya_alamat()
mahasiswa1.sebutNim()
