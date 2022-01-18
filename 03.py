class susunInput:
    def __init__(self, inputHitung):
        #Variabel Encapsulation
        self.__operan1= inputHitung.split()[0]
        self.__operator= inputHitung.split()[1]
        self.__operan2= inputHitung.split()[2]
    def hitung(self):
        if self.__operator == "+":
            return float(self.__operan1) + float(self.__operan2)
        elif self.__operator == "-":
            return float(self.__operan1) - float(self.__operan2)
        elif self.__operator == "*":
            return float(self.__operan1) * float(self.__operan2)
        elif self.__operator == "/":
            return float(self.__operan1) / float(self.__operan2)

#Class Inherintance
class masukkanInput(susunInput):
    def __init__(self):
        self.inputHitung= input("Masukkan perhitungan [ (operan1) (spasi) (operator) (spasi) (operan2) ]: ")
        susunInput.__init__(self, self.inputHitung)
        self.operator= self.inputHitung.split()[1]
        if self.operator == "+":
            self.operator= "Tambah"
        elif self.operator == "-":
            self.operator= "Kurang"
        elif self.operator == "*":
            self.operator= "Kali"
        else:
            self.operator= "Bagi"

kalkulator1= masukkanInput()
print("\n" + str(kalkulator1.hitung()))
print("Jenis operasi adalah " + kalkulator1.operator)
