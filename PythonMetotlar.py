class personel:

    def __init__(self, tc, ad, soyad, yas, departman, maas):
        self.tc = tc
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.departman = departman
        self.maas = maas

    def personel_bilgi(self):
        print(f"{self.tc}, {self.ad}, {self.soyad}, {self.yas}, {self.departman}, {self.maas} ")

    def maas_arttir(self, miktar):
        self.maas += miktar
        print(f"{self.ad} {self.soyad} maaşı {miktar} zamlı maaşı {self.maas} ")



personel1 = personel("11111111111", "ayhan", "akkaya", 40, "yazılımcı", 100000)
personel2 = personel("14189949432", "şevket", "şekerciler", 19, "muhasebeci", 10)
personel3 = personel("22222222222", "muhammed", "gök", 19, "insankaynakları", 5)

personel1.personel_bilgi()
personel2.personel_bilgi()
personel3.personel_bilgi()

personel1.maas_arttir(500)
personel2.maas_arttir(300)
personel3.maas_arttir(700)
