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


def kayitGetir():

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")

    cursor = baglan.cursor()

    cursor.execute("Select * From products")  #products tablosundan seç neyi * yani her şeyi sorguyu yaptık şimdi çalıştırak

    sonuc = cursor.fetchall()  # birden fazla kayıt almak istediğimiz zaman kullandığımız bir metot

    print(sonuc)           # yan yana yazar karışık gözüküyor
    for products in sonuc: # alt alta yazar daha derli toplu
        print(products)

    for products in sonuc: # böyle yaparak istediğimiz yerleri alabiliriz
        print(f"model:{products[1]} fiyat: {products[2]}")


    cursor.execute("SELECT ad,fiyat FROM products") # yukarıda bütün sütunları aldık ama sadece ad ve fiyatı yazdırdık
#                                                 e kalan sütunlar ne işe yarıyor hiçbir işe boş gereksiz iş oluyor
    sonuc = cursor.fetchall()
                           

    for products in sonuc:
        print(f"model:{products[0]} fiyat: {products[1]}")
        

    cursor.execute("SELECT ad,fiyat FROM products")
    result = cursor.fetchone()                     # sadece bulduğu ilk kaydı bize getirir onun için one
    print(f"model:{result[0]} fiyat: {result[1]}") # ad fiyat dışında bir şey yazdırmaya çalışsaydık hata verirdi
#                                                  çünkü öyle bir şey almadık IndexError: tuple index out of range

kayitGetir()