# Inheritance (kalıtım) miras alma


class insan:

    def __init__(self, adi,soyadi,):
        self.ad=adi
        self.soyad=soyadi
        print("insan oluşturuldu")
    
    def ben_kimim(self):                    # fonksiyon yazarken self i kullanmazsan hata verir
        print("ben kimim anlatiyim insan")

    def yerim(self):
        print("ben insanım yerim")

class ogrenci(insan):

    def __init__(self,isim,soyisim,numara):
        insan.__init__(self,isim,soyisim) # isim ve soyisimi bir daha self.ad vs uğraşmadan kalıtım aldığımız sınıfın
                                          # constructor ına yolladık 
        self.no=numara

        print("ogrenci olusturuldu")

    # override ezme işlemi
    def ben_kimim(self):
        print("ben kimin anlatiyim ogrenci")

    def merhaba(self):
        print("merhaba ben bir ogrenciyim")


class ogretmen(insan):
    def __init__(self,adi,soyadi,branş):
        super().__init__(adi,soyadi)       # önceki gibi insan.init yerine bu kullanımı da yapabiliriz
        self.branş = branş                 # super().__init__(a,b) eğer super ile yaparsan
                                           # " self eklemek zorunda değilsin " sadece parametreler yeterli
    def ben_kimim(self):
        print(f"ben kimim anlatiyim {self.branş} ogretmeni")


i1 = insan("fatih","yeni")
ogr1 = ogrenci("cemre","yeni","1")
ogrt = ogretmen("saliha","yeni","beden")

print(i1.ad + " " + i1.soyad)
print(ogr1.ad + " " + ogr1.soyad + ogr1.no)

i1.ben_kimim()
ogr1.ben_kimim()
ogrt.ben_kimim()

i1.yerim()
ogr1.yerim()

ogr1.merhaba()

