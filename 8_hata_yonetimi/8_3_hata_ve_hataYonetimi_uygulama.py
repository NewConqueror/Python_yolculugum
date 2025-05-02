liste = ["1","2","5a","10b","abc","10","50"]

# 1 liste elemanları içindeki sayısal değeleri bulunuz

for i in liste:
    try:
        int(i)  # kendi otomatik hata döndürdüğü için raise hata vs dememize gerek yok
        print(i)
    except:
        continue

# 2 kullanıcı q değerini girmedikçe aldığınız her inputun sayı old emin olunuz aksi halde hata mesajı yollayın

while True:
    x= input("sayi: ") 
    if(x=="q"):
        break
    try:
        sonuc = int(x)
        print("girdiginiz sayi: ",sonuc)
        break
    except:
        print("geçersiz sayi")



# 3 girilen parola içinde türkçe karakter hatası veriniz

def parolaKontrol(parola):
    turkceKarakterler = "ıöüğçşİ"
    for i in parola:
        if i in turkceKarakterler:
            raise TypeError("parola türkçe karakter içeremez") # kendi otomatik hata döndürmediği için 
        else:                                                  # hatayı bizim döndürmemiz gerekti
            pass                                               # fonk içinde kullanımda böyle yapman lazım
        #                                                     oto hata döndüren bir şey yoksa tabii ki




sifre = input("sifre: ")

try:
    parolaKontrol(sifre)
except TypeError as error:
    print(error)

    

# 3 faktoriyel fonk oluşturup fonk a gelen değer için hata mesajları verin


def faktoriyel(x):

    x = int(x)
    if(x < 0):
        raise ValueError("sayi negatif olamaz") # oto hata döndüren bir şey olmadığı için hatayı biz fırlattık
    sonuc = 1

    for i in range(1,x+1):
        sonuc*=i
    
    return sonuc


for i in [5,10,20,-3,"10a"]:
    try:
        a = faktoriyel(i)  
    except ValueError as err: # invalid literal for int() with base 10: '10a' int a çeviremediği için bu hatayı yollar
        print(err)
        continue
    print(a)




