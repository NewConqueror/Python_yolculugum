import mysql.connector

def kayityap(ad, fiyat, url, aciklama):

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")

    mycursor = baglan.cursor()

    sql = "INSERT INTO products (ad,fiyat,url,aciklama) VALUES(%s,%s,%s,%s)"
    
    values = (ad, fiyat, url, aciklama)
    # values = ("samsun s7",3000,"url aq","iyi iyi iyi") # kayitlari yapti

    mycursor.execute(sql, values) # sorgu hazırladık ama daha çalıştırmadık execute gördün diye hemen mi çalışacak

    try:
        baglan.commit() # sorgu gerçekten database e gönderiliyor

        print(f"{mycursor.rowcount} tane kayit eklendi")      # rowcount adı üstünde kayitlari sayar
        print(f"son eklenen kaydin id: {mycursor.lastrowid}") # son eklenen kaydın id sini döndürür

    except mysql.connector.Error as hata:
        print("hata: ",hata)

    finally:
        baglan.close()  # her şartta baglantiyi kapayalım
        print("database baglantisi kapandi")    

def kayitlaryap(liste):

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")

    mycursor = baglan.cursor()

    sql = "INSERT INTO products (ad,fiyat,url,aciklama) VALUES(%s,%s,%s,%s)"
    
    values = liste        # direkt listeden kendi alıyor
    # values = ("samsun s7",3000,"url aq","iyi iyi iyi") # kayitlari yapti

    mycursor.executemany(sql, values) # çoğul kayıt yapıcaksak executemany komutu ile yaparız

    try:
        baglan.commit() # sorgu gerçekten database e gönderiliyor

        print(f"{mycursor.rowcount} tane kayit eklendi")      # rowcount adı üstünde kayitlari sayar
        print(f"son eklenen kaydin id: {mycursor.lastrowid}") # son eklenen kaydın id sini döndürür

    except mysql.connector.Error as hata:
        print("hata: ",hata)

    finally:
        baglan.close()  # her şartta baglantiyi kapayalım
        print("database baglantisi kapandi")    



liste = []  # her kayıt için baglan nesnesi mi oluşturucaz aq onun yerine kayıtları bir listeye atarım
#             sonda hepsini beraber kayıt ederim database e sürekli git gel yapmaktan daha mantıklı   

while True:
    ad = input("ürün ad      : ")
    fiyat = input("ürün fiyat   : ")
    url = input("ürün url     : ")
    aciklama = input("ürün aciklama: ")

    liste.append( (ad, fiyat, url, aciklama) ) # bir tuple listesine çevirdik

    secim = input("devam etmek ister misiniz: (e/h)")
    
    if(secim=="h"):
        print("kayitlariniz veri tabanina aktariliyor")
        print(liste) # gördüğün gibi tuple tipinde
        kayitlaryap(liste)
        break

#kayityap(ad, fiyat, url, aciklama)