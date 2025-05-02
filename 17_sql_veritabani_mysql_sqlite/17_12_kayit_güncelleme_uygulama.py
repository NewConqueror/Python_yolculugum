import mysql.connector
from datetime import datetime

baglanti = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="mysql2004",
    database = "okul"     
    )

class ogrenci:

    bağlan = baglanti
    mycursor = bağlan.cursor()
    
    def __init__(self,id,numara,ad,soyad,dogumTarihi,cinsiyet):

        if id is None:
            self.id = 0
        else:
            self.id = id

        self.numara = numara
        self.ad = ad
        self.soyad = soyad
        self.dogumTarihi = dogumTarihi
        self.cinsiyet = cinsiyet

    def kayityap(self):
        sql = "INSERT INTO ogrenci(numara,ad,soyad,dogumTarihi,cinsiyet) VALUES(%s,%s,%s,%s,%s)"
        
        deger = (self.numara, self.ad, self.soyad, self.dogumTarihi, self.cinsiyet)

        ogrenci.mycursor.execute(sql,deger)

        try:
            ogrenci.bağlan.commit()
            print(f"{ogrenci.mycursor.rowcount} tane kayit eklendi")

        except mysql.connector.Error as hata:
            print("hata: ",hata)
            
        finally:
            ogrenci.bağlan.close()

    @staticmethod         # 
    def kayitlaryap(liste):
        sql = "INSERT INTO ogrenci(numara,ad,soyad,dogumTarihi,cinsiyet) VALUES(%s,%s,%s,%s,%s)"
        
        degerler= liste

        ogrenci.mycursor.executemany(sql,degerler)

        try:
            ogrenci.bağlan.commit()
            print(f"{ogrenci.mycursor.rowcount} tane kayit eklendi")

        except mysql.connector.Error as hata:
            print("hata: ",hata)
            
        finally:
            ogrenci.bağlan.close()

   
    @staticmethod
    def ogrenciInfo():
        sql = "SELECT * FROM ogrenci LIMIT 5" # ekstra bilgi sadece ilk 5 kayıt ile limitler kalanı getirmez 
        # 4- Aşağıdaki sorguları yazınız.
        #   a- Tüm öğrenci kayıtlarını alınız.
        #   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
        #   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
        #   d- 2003 doğumlu öğrenci bilgilerini alınız. 
        #   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
        #   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
        #   g- Kaç erkek öğrenci vardır ?
        #   h- Kız öğrencileri harf sırasına göre getiriniz.

        sql = "SELECT * from ogrenci"

        sql = "SELECT numara,ad,soyad from ogrenci"

        sql = "SELECT ad,soyad from ogrenci where cinsiyet='K'"

        sql = "SELECT * from ogrenci where YEAR(dogumTarihi)=2003" #YEAR methodu datetimeın içinden yıl bilgisini alır MONTH DATE vs de olur

        sql = "SELECT * from ogrenci where ad='ali' and YEAR(dogumTarihi)=2005"

        sql = "SELECT * from ogrenci where ad like '%an%' or soyad like '%an%' "

        sql = "SELECT COUNT(*) from ogrenci where cinsiyet='E'"

        sql = "SELECT * from ogrenci where cinsiyet=K order by ad,soyad"


        ogrenci.mycursor.execute(sql)

        try:
            sonuc = ogrenci.mycursor.fetchall()
            
            for x in sonuc:
                print(x )

        except mysql.connector.Error as hata:
            print("hata: ",hata)
        
        finally:
            ogrenci.bağlan.close()

    @staticmethod
    def kayitgetirId(id):
        # 5- Aşağıdaki güncelleme sorularını yapınız.
        #   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
        #   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

        sql = "select * from ogrenci where id=%s"

        value = (id,)

        ogrenci.mycursor.execute(sql,value)

        try:
            sonuc = ogrenci.mycursor.fetchone()
            
            return ogrenci(sonuc[0],sonuc[1],sonuc[2],sonuc[3],sonuc[4],sonuc[5]) # (7,277,fatih,yeni,dt,cins)

        except mysql.connector.Error as hata:
            print("hata: ",hata)
        


    def ogrenciGuncelle(self):

        sql = "update ogrenci set numara=%s, ad=%s, soyad=%s, dogumTarihi=%s, cinsiyet=%s, where id=%s"

        values =(self.numara, self.ad, self.soyad, self.dogumTarihi, self.cinsiyet, self.id)

        ogrenci.mycursor.execute(sql,values)

        try:
            ogrenci.bağlan.commit()
            print(f"{ogrenci.mycursor.rowcount} tane kayit güncellendi")

        except mysql.connector.Error as hata:
            print("hata: ",hata)


    @staticmethod
    def kayitlariGetirCinsiyet(cinsiyet):
      
        sql = "select * ogrenci where cinsiyet=%s"

        value = (cinsiyet,)

        ogrenci.mycursor.execute(sql,value)

        try:
            return ogrenci.mycursor.fetchall()  # fetchall dan dolayı bir liste dönecek
            

        except mysql.connector.Error as hata:
            print("hata: ",hata)

    @staticmethod
    def ogrenciLERiGuncelle(liste):

        sql = "update ogrenci set numara=%s, ad=%s, soyad=%s, dogumTarihi=%s, cinsiyet=%s, where id=%s"

        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
        
            item = [item[i] for i in order]
            values.append(item)


        ogrenci.mycursor.executemany(sql,values)

        try:
            ogrenci.bağlan.commit()
            print(f"{ogrenci.mycursor.rowcount} tane kayit güncellendi")

        except mysql.connector.Error as hata:
            print("hata: ",hata)
        



        
# nesne = ogrenci.kayitgetirId(7)
# print(nesne) # bir tuple listesi gelir




ogr = ogrenci.kayitgetirId(7)     # self eşitlemesi yapıyorsun da denilebilir

ogr.ad = "cemre"
ogr.soyad = "yeni"

ogr.ogrenciGuncelle()


ogrliste = ogrenci.kayitlariGetirCinsiyet("E")
print(ogrliste)


liste = []

for ogrnc in ogrliste:

    ogrnc = list(ogrnc) 

    ogrnc[2] = "bay" + ogrnc[2]

    liste.append(ogrnc)


ogrenci.ogrenciLERiGuncelle(liste)