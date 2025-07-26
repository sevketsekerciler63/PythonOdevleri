marks = 90
attendance_percentage = 87
if marks >= 80 and attendance_percentage >= 85:
    print("onur için uygun")
else:
    print("Onur için uygun değil")






class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)







def greet(name):
    print("Merhaba,", name)

greet("Alice")







5 == 5

age = 25
age == 30




for num in range(1, 10):
    print(num)

fruits = ["elma", "muz", "portakal", "üzüm", "kivi"]
for fruit in fruits:
    print(fruit)






5 >= 5 and 9 >= 5

quantity = 105
minimum = 100
quantity >= minimum









9 > 6

age = 20
max_age = 25
age > max_age









score = 85
if score >= 90:
    print("A aldınız!")
elif score >= 80:
    print("B aldınız.")
else:
    print("Daha çok çalışmalısınız.")







age = 18
if age >= 18:
    print("Yetişkinsiniz.")
else:
    print("Henüz yetişkin değilsiniz.")









5 <= 5 and 3 <= 5

size = 38
max_size = 40
size <= max_size






4 < 6

score = 60
passing_score = 65
score < passing_score




for num in range(1, 6):
    if num == 3:
        break
    print(num)

for num in range(1, 6):
    if num == 3:
        continue
    print(num)



isLocked = False
print(not isLocked)



a = 10
b = 20
a != b

count = 0
count != 0




grade = 12
if grade == 11 or grade == 12:
    print("Veda Partisi Davetiyesi")
else:
    print("Uygun değil")


list(range(5))

list(range(2, 10))

list(range(1, 11, 2))

def add(a, b):
    return a + b

result = add(3, 5)



try:
    num = int(input("Bir sayı girin: "))
except ValueError:
    print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")



try:
    num = int(input("Bir sayı girin: "))
except ValueError:
    print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")
else:
    print("Girdiğiniz sayı:", num)



try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Dosya bulunamadı.")
finally:
    file.close()

count = 0
while count < 5:
    print(count)
    count += 1

    sonuc = "Merhaba" + " John"

    x = 7
    y = 12.4
    gecerli_mi = True
    gecerli_mi = False
    Ad = "John"

    benim_dizem = "Merhaba"
    karakter = benim_dizem[0]
    uzunluk = len(benim_dizem)

    kucuk_harfli_metin = benim_dizem.lower()

    print("Merhaba, dünya")
    print(x + y)

    x = 9
    y = 4
    sonuc_topla = x + y
    sonuc_cikar = x - y
    sonuc_carp = x * y
    sonuc_bol = x / y
    sonuc_tam_bol = x // y
    sonuc_mod = x % y

    yeni_metin = benim_dizem.replace("Merhaba", "Selam")

    alt_dize = benim_dizem[0:5]

    ayrilmis_metin = benim_dizem.split(",")

    kisaltmis = benim_dizem.strip()

    buyuk_harfli_metin = benim_dizem.upper()

    isim = "John"
    x = 5