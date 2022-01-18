def hitungLuas(panjang, lebar):
    return str(panjang * lebar)

def hitungKeliling(panjang, lebar):
    return str(2 * (panjang + lebar))

panjang= int(input("Masukkan nilai panjang: "))
lebar= int(input("Masukkan nilai lebar: "))
print("Keliling persegi panjang adalah: " + hitungKeliling(panjang, lebar))
print("Luas persegi panjang adalah: " + hitungLuas(panjang, lebar))
