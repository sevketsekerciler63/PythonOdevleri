colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(color)


for number in range(1, 11):
    print(number)



for number in range(11):
    print(number)




for number in range(1, 11):
    print(number)



fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")




count = 1
while count <= 10:
    print(count)
    count += 1









yas = 25
if yas == 25:
    print("Sen 25 yaşındasın.")



if yas != 30:
    print("Sen 30 yaşında değilsin.")


if yas >= 20:
    print("Evet, yaş 20'den büyük veya eşit.")



yas = 20
if yas >= 21:
    print("Bar'a girebilirsin.")

else:
    print("Üzgünüm, Bar'a giremezsin.")



if yas >= 21:
    print("Bar'a girebilirsin.")

elif yas >= 18:
    print("Film izleyebilirsin.")


else:
    print("Üzgünüm, ikisini de yapamazsın.")




kullanici_secimi = "Nakit Çek"
if kullanici_secimi == "Nakit Çek":
    miktar = int(input("Çekmek istediğiniz miktarı girin: "))
    if miktar % 10 == 0:
        print("Verilen miktar: ", miktar)
    else:
        print("Lütfen 10'un katı bir miktar girin.")
else:
    print("ATM'yi kullandığınız için teşekkürler.")






rahatsiz_etme_modu = True
if not rahatsiz_etme_modu:
    print("Yeni mesaj bildirimi gönderildi.")



gecerli_kimlik_karti = True
eslesen_parmak_izi = True
if gecerli_kimlik_karti and eslesen_parmak_izi:
    print("Yüksek güvenlikli kapı açıldı.")


arkadas1_komedi_seviyor = True
arkadas2_aksiyon_seviyor = False
arkadas3_drama_seviyor = False
if arkadas1_komedi_seviyor or arkadas2_aksiyon_seviyor or arkadas3_drama_seviyor:
    print("Bir film seçildi.")
