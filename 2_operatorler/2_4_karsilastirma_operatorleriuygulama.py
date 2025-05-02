
a = int(input("1.sayi: "))
b = int(input("2.sayi: "))
sonuc = (a>b)

print(f"a: {a} b den {b} büyüktür: {sonuc}")

vize1= int(input("1.vize: "))
vize2 = int(input("2.vize: "))
final = int(input("final:  "))

ortalama = ((vize1+vize2)/2)*0.6 + final*0.4

print(f"not ortalamanız: {ortalama} geçme durumu : {ortalama>=50}")


sayi = int(input("sayi: "))

sonuc = (sayi%2==0)

print(f" çift mi : {sonuc}")


deger = int(input("deger: "))

sonuc = (deger>0)

print(f"pozitif mi {sonuc}")

email = input("email : ")
parola =input("parola: ")

emailkontrol = (email.strip()== "email@sadikturan.com") # boşluk falan varsa onları sildi ki yanlış olmasın
parolakontrol = (parola.lower()== "abc123") # büyük küçük harf yanlışı olmasın dedik

print(f"email doğru mu:  {emailkontrol} parola doğru mu : {parolakontrol}")