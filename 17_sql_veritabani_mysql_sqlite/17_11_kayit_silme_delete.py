import mysql.connector

def kayitSil(id):

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")
    cursor = baglan.cursor()
    
    sql = "delete from products where id=4" # id si 4 olan kayıtı bul ve o kayıtı sil

    sql = "delete from products where ad like '%iphone%'" # adında iphone geçen kayıtları bul ve o kayıtları sil

    sql = "delete from products where id=%s"   #"... id=" +id dersen de olur ama hatalı şeyler olabilir böyle daha iyi

    value = (id,)

    cursor.execute(sql)


    cursor.execute(sql,value)
    
    try:
        baglan.commit()
        print(f"{cursor.rowcount} tane kayit güncellendi")

    except mysql.connector.Error as hata:
        print("hata: ",hata)

    finally:
        baglan.close()
        print("database bağlantisi kapandi")


kayitSil(5)  # biz hangi id değerini verirsek o id li kayıtı silecek