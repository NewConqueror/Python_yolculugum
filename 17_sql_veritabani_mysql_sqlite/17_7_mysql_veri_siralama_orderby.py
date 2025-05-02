import mysql.connector

def kayitGetir():

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")

    cursor = baglan.cursor()

    cursor.execute("select * from products order by ad")         # ad a göre sıralar

    cursor.execute("select * from products order by fiyat")      # fiyata göre sıralar

    cursor.execute("select * from products order by id")         # id ye göre sıralar
    
    cursor.execute("select * from products order by id ASC")     # yine id ye yukarıdaki ile aynı artan şekilde 1 2

    cursor.execute("select * from products order by id DESC")    # id ye göre sıralar ama bu sefer azalan şekilde 9 8
    
    cursor.execute("select * from products order fiyat DESC") # fiyat için sıralar azalan şekilde

    cursor.execute("select * from products order by ad, fiyat")  # önce ad a göre o adları da kendi içinde fiyata göre
    
    try:
        sonuc = cursor.fetchall() 
        for product in sonuc:
            print(f"id: {sonuc[0]} model:{sonuc[1]} fiyat: {sonuc[2]}")

    except mysql.connector.Error as hata:
        print("hata: ",hata)

    finally:
        baglan.close()
        print("database bağlantisi kapandi")