from ders120_veri_tabanı_yonetici import veritabaniyonetici
from ders120_ogrenci import ogrenci
import datetime

class uygulama:

    def __init__(self):
        self.db = veritabaniyonetici()

    def uygulamagiris(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.ogrencilistele()
            elif islem == '2':
                self.ogrenciekle()
            elif islem == '3':
                self.ogrenciguncelle() 
            elif islem == '4':
                self.ogrencisil()
            elif islem == 'E' or islem =='Ç':
                break
            else:
                print('yanlış seçim')


    def ogrencisil(self):
        sinifid = self.ogrencilistele()
        ogrid = int(input('öğrenci id: '))

        self.db.ogrencisil(ogrid)

    def ogrenciguncelle(self):

        sinifid = self.ogrencilistele()
        
        ogrid = int(input("öğrenci id: "))

        ogr = self.db.ogrencigetirid(ogrid) # liste dönüyor

        ogr[0].ad = input('ad:') or ogr[0].ad  # ad girilirse güncellenicek girilmezse normal kendi adı
        ogr[0].soyad = input('soyad:') or ogr[0].soyad
        ogr[0].cinsiyet = input('cinsiyet (E/K):') or ogr[0].cinsiyet
        ogr[0].sinifid = input('sınıf: ') or ogr[0].sinifid

        yil = input("yıl: ") or ogr[0].dogumTarihi.yil
        ay = input("ay: ") or ogr[0].dogumTarihi.ay
        gün = input("gün: ") or ogr[0].dogumTarihi.gün

        ogr[0].dogumTarihi = datetime.date(yil,ay,gün)
        self.db.ogrenciguncelle(ogr[0]) 

    def ogrenciekle(self):

        self.siniflistele()

        sinifid = input("hangi sınıf: ")

        numara = input("numara:")
        ad = input("ad: ")
        soyad = input("soyad: ")
        yil = int(input("yil: "))
        ay = int(input("ay: "))
        gün = int(input("gün: "))

        dogumTarihi = datetime.date(yil,ay,gün)
        cinsiyet = input("cinsiyet (E/K): ")

        ogr = ogrenci(None,numara,ad,soyad,dogumTarihi,cinsiyet,sinifid)

        self.db.ogrenciekle(ogr)

    def siniflistele(self):
        
        siniflar = self.db.siniflarigetir() # geriye bir liste dönüyor

        for i in siniflar:
            print(f"{i.id}: {i.ad}")

    def ogrencilistele(self):
        
        self.siniflistele()

        sinifid = int(input("hangi sınıf: "))
       
        ogrenciler = self.db.ogrenciLERigetirsinifid(sinifid) # listenin içi boş aq (edit: hallettim sıkıntı yok)

        print("öğrenci listesi")
        print(ogrenciler)
        for ogr in ogrenciler:
            
            print(f"{ogr.id}: {ogr.ad} {ogr.soyad}")

        return sinifid


app = uygulama()    
app.uygulamagiris()

