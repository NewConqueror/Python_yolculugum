def usal(sayi):

    def iç(us):
        return sayi ** us
    
    return iç # burda da fonksiyonu döndürüyoruz

iki = usal(2) # şu an  iki = iç fonksiyonu oldu ikisi de aynı işi yapıyor
print(iki(4)) #  2^4 yani 16 döndürür usal(2(4)) gibi düşünebilirsin

bes = usal(5)
print(bes(3)) # 5^3 yani 125 döndürür


def yetki_sorgula(sayfa):

    def rol_sorgula(rol):
        if(rol=="admin"):
            print("{0} rolü {1} sayfasina ulaşabilir".format(rol,sayfa))
        else:
            print("{0} rolü {1} sayfasina ulaşamaz".format(rol,sayfa))

    return rol_sorgula

user1 = yetki_sorgula("product edit") # şuan  user1 = rol_sorgula fonksiyonu olarak işe yarar
user1("admin") # rol_sorgula("admin") gibi düşünebilirsin

user2 = yetki_sorgula("product edit")
user2("user")



def islem(islemadi):

    def toplama(*args): # *args yani tuple liste tipinde sıralı 1,3,5,7 gibi
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    if(islemadi == "toplama"):
        return toplama
    else:
        return carpma
    

toplama = islem("toplama") # toplama değişkeni artık toplama Fonksiyonunu temsil ediyor
print(toplama(1,2,3,4,5,6,7,8,9,10))

carpma = islem("carpma") # carpma değişkeni artık carpma Fonksiyonunu temsil ediyor
print(carpma(1,5,2,10))
