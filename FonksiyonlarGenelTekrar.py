def merhaba():
    print("Selam dostum!")

merhaba()



def topla(a, b):
    return a + b

print(topla(10, 25))

metin = "Python"
uzunluk = len(metin)
print(uzunluk)

sayilar = [5, 10, 20]
toplam = sum(sayilar)
print(toplam)

degerler = [7, 3, 11, 42, 1]
print(max(degerler))
print(min(degerler))




def carp(a, b):
    return a * b

sonuc = carp(6, 7)
print(sonuc)

def kare_al(n):

    return n ** 2

print(kare_al(8))




mesaj = "Ben globalim"

def yaz():
    yerel = "Ben yerelim"
    print(mesaj)
    print(yerel)

yaz()
print(mesaj)


my_list = []

def ekle(liste, eleman):
    liste.append(eleman)

ekle(my_list, 12)
ekle(my_list, 99)
print(my_list)





def sil(liste, eleman):
    if eleman in liste:
        liste.remove(eleman)
    else:
        print("Eleman bulunamadı.")

sil(my_list, 12)
sil(my_list, 500)
print(my_list)

def yazdir(limit):
    for i in range(1, limit + 1):
        print(i)

yazdir(5)





def selamla(kisi):
    return "Merhaba " + kisi

for _ in range(3):
    print(selamla("Zeynep"))

sayilar = []





def pozitif_ekle(liste, sayi):
    if sayi > 0:
        liste.append(sayi)
    else:
        print("Negatif sayı eklenemez.")

pozitif_ekle(sayilar, 10)
pozitif_ekle(sayilar, -5)
print(sayilar)