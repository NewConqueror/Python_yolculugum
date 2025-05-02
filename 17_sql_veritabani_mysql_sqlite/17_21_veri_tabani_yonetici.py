import mysql.connector
from datetime import datetime
from ders120_baglanti import baglanti
from ders120_ogrenci import ogrenci
from ders120_ogretmen import ogretmen
from ders120_sinif import sinif

class veritabaniyonetici():

    def __init__(self):
        
        self.connection = baglanti
        self.cursor = self.connection.cursor()

    def ogrencisil(self,ogrenciid):
        sql = "delete from ogrenci where id=%s"
        value = (ogrenciid,)
        self.cursor.execute(sql,value)
    
    def ogrencigetirid(self,id):

        sql = "select * from ogrenci where id=%s"
        value = (id,)

        self.cursor.execute(sql,value)

        try:
            nesne = self.cursor.fetchone() # bir tuple listesi gelir
            return ogrenci.ogrenciOlustur(nesne)  # tuple sa listeye ekleyecek
        
        except mysql.connector.Error as hata:
            print("hata: ",hata)


    def ogrenciLERigetirsinifid(self,sinifid):

        sql = "select * from ogrenci where sinifid=%s"
        value = (sinifid,)

        self.cursor.execute(sql,value)

        
        try:
            nesne = self.cursor.fetchall() # bir liste şeklinde id numara ad soyad datetime hepsi var 
            print(nesne)
            return ogrenci.ogrenciOlustur(nesne) # tuple sa listeye ekleyecek değilse de listeye ekleyecek yazdırıcak
            

        except mysql.connector.Error as hata:
            print("hata: ",hata)



    def siniflarigetir(self):

        sql = "select * from sinif"
        

        self.cursor.execute(sql)

        try:
            nesne = self.cursor.fetchall()
           # print(nesne)
            return sinif.sinifOlustur(nesne) # eğer tuple değilse for ile dönücek ve yazdıracak

        except mysql.connector.Error as hata:
            print("hata: ",hata)
    
        

    def ogrenciekle(self, ogr: ogrenci):
        sql = "insert into ogrenci(numara,ad,soyad,dogumTarihi,cinsiyet,sinifid) values(%s,%s,%s,%s,%s,%s)"
        
        values = (ogr.numara,ogr.ad,ogr.soyad,ogr.dogumTarihi,ogr.cinsiyet,ogr.sinifid)

        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")

        except mysql.connector.Error as hata:
            print("hata: ",hata)


    def ekleYadaGuncelle(self,ogr: ogrenci):
        pass


    def ogrenciguncelle(self, ogr: ogrenci):
        
        sql = "update ogrenci set numara=%s,ad=%s,soyad=%s,dogumTarihi=%s,cinsiyet=%s,sinifid=%s where id=%s"

        values = (ogr.numara,ogr.ad,ogr.soyad,ogr.dogumTarihi,ogr.cinsiyet,ogr.sinifid,ogr.id)

        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi")
        
        except mysql.connector.Error as hata:
            print("hata: ",hata)

    def ogretmenekle(self, ogrt: ogretmen):
        pass

    def ogretmenguncelle(self, ogrt: ogretmen):
        pass

    
    def __del__(self):

        self.connection.close()
        print("baglanti silindi")



db = veritabaniyonetici()

ogr = db.ogrencigetirid(23) # artık 23 id nin self i yaptık diyebiliriz

ogr[0].ad = "cemre"
ogr[0].soyad = "yeni"

# db.ogrenciekle(ogr[0])
db.ogrenciguncelle(ogr[0])


# print(ogr[0].ad)
# print(ogr[0].soyad)


# ogrler = db.ogrenciLERigetirsinifid(1)  # bize bir liste gelir

# print(ogrler[0].name) # ilk kaydın adı
# print(ogrler[4].name) # 4.kaydın adı