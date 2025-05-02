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
    
    def __init__(self,numara,ad,soyad,dogumTarihi,cinsiyet):
        
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

        sql = "SELECT * from ogrenci where YEAR(dogumTarihi)=2003" #YEAR methodu datetimeın içinden yıl bilgisini alır MONTH DAY vs de olur

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


        




# ahmet = ogrenci("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E")
# ahmet.kayityap()

# baglanti = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password ="mysql2004",
#     database = "okul"     
#     )

# imlec = baglanti.cursor()

# sql = "INSERT INTO ogrenci(numara,ad,soyad,dogumTarihi,cinsiyet) VALUES(%s,%s,%s,%s,%s)"

ogrenciler = [
    
    ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
]

# imlec.executemany(sql,ogrenciler) # sonucta bir liste vermiş olduk executemany kullandık dikkat et

# try:
#     baglanti.commit()
#     print(f"{imlec.rowcount} tane kayit eklendi")
    
# except mysql.connector.Error as hata:
#     print("hata: ",hata)

# finally:
#     baglanti.close()

ogrenci.kayitlaryap(ogrenciler)