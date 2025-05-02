# 1 ile 100 arası sayı  hak kullanıcıdan  aşağı yukarı dicen her soru 20 puan 100 üzerinden

import random

sayi = random.randint(1,100)    
print(sayi)
hak = int(input("hak sayisini giriniz: "))
sayac=0
while hak>0:
    sayac+=1
    
    tahmin = int(input("tahmininiz: "))

    if(tahmin>sayi):
        print("asaği")
    elif(tahmin<sayi):
        print("yukari")
    else:
        print(f"tebrikler {sayac}.defada sayiyi buldunuz puaniniz:{100-(20*(sayac-1))}")
        break
    

    hak-=1

    if(hak==0):
        print(f"üzgünüz kaybettiniz sayi {sayi} idi")
        break



sayi = int(input("sayiyi giriniz: "))

asalmi = True

if(sayi<2):
    print("2 den küçük asal sayi olamaz")

for i in range(2,sayi): # 2 den başla sayiya kadar git birer birer default u bir çünkü    
    if(sayi%i==0):
        asalmi=False
        break

if asalmi: # True ise çalışacak False ise çalışmayacak
    print(f"sayi asaldir {sayi}")
else:
    print("sayi asal değildir")