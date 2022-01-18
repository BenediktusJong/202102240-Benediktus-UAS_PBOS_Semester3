class susunInput:
    def __init__(self, inputHitung):
        self.__operan1= inputHitung.split()[0]
        self.__operator= inputHitung.split()[1]
        self.__operan2= inputHitung.split()[2]
    def hitung(self):
        if self.operator == "+":
            return self.__operan1 + self.operan2

class masukkanInput(susunInput):
    
    def __init__(self):
        self.inputHitung= input("Masukkan perhitungan [ (operan1) (spasi) (operator) (spasi) (operan2) ]: ")
        susunInput.__init__(self, self.inputHitung)


kalkulator1= masukkanInput()
print(kalkulator1.hitung)
