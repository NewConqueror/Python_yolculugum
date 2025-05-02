import mysql.connector

def kayitGüncelle(id, ad, fiyat):

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")
    cursor = baglan.cursor()

    if ad!="":  # if not name: de olur boşluk false demek çünkü
        sql = "update products set ad='samsung s10' where id=5"

    if fiyat>5000:
        pass # vs vs vs
    
    sql = "update products set ad='samsung s10' where id=5" # id si 5 olan yere git ve ad kısmına samsung s10 yaz

    sql = "update products set ad='iphone 15', fiyat=10000 where id=2" 
    # id si 2 olan yere git ve ad kısmına iphone 15 fiyat kısmına ise 10000 yaz

    sql = "update products set ad=%s, fiyat=%s where id=%s"

    values = (ad, fiyat, id)

    cursor.execute(sql,values)
    
    cursor.execute(sql)

    try:
        baglan.commit()
        print(f"{cursor.rowcount} tane kayit güncellendi")

    except mysql.connector.Error as hata:
        print("hata: ",hata)

    finally:
        baglan.close()
        print("database bağlantisi kapandi")

kayitGüncelle(3,"huawei y6",5000)

kayitGüncelle(3,"",5000)