import mysql.connector


def kayitGetir():

    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")

    cursor = baglan.cursor()

    cursor.execute("Select * From products where id=1") # sadece id bilgisi 1 olan kayıt gelir
    sonuc = cursor.fetchall()
                           

    cursor.execute("Select * From products where ad='redmi10'") # sadece adı redmi10 olan kayıtlar gelir
    sonuc = cursor.fetchall()


    cursor.execute("Select * From products where ad='redmi10' and fiyat=3000")
    # adı redmi10 olan ve fiyatı 3000 olan kayıtlar gelir >  <  >=  vs de kullanılır
    sonuc = cursor.fetchall()


    cursor.execute("Select * From products where ad='redmi10' or fiyat>3000")
    # adı redmi10 olan veya fiyatı 3000 den büyük olan kayıtlar gelir
    sonuc = cursor.fetchall()


    cursor.execute("Select * From products where ad LIKE '%Samsung%' ")
    # başta ve sonda % işareti olması demek uzun bir açıklama var içerisinde Samsung geçen kayıtları bize getir
    sonuc = cursor.fetchall()


    cursor.execute("Select * From products where ad LIKE 'Samsung%' ")
    # sadece başta % işareti olması demek en başı samsung olucak sonu ne olursa olsun öyle kayıtları getirir
    sonuc = cursor.fetchall()


    cursor.execute("Select * From products where ad LIKE '%Samsung' ")
    # sadece sonda % işareti olması demek sonu samsung olucak başı ne olursa olsun böyle kayıtları getirir
    sonuc = cursor.fetchall()


    print(sonuc) # bize bir liste şeklinde gelir ve for döngüsü kullanmak zorunda kalırız tek 1 kayıt bile olsa
    
    sonuc = cursor.fetchone()
    print(sonuc) # liste şeklinde gelmez yani bunu direkt yazdırabiliriz for döngüsüne gerek yok


    cursor.execute("Select * From products where id=1")
    sonuc = cursor.fetchone() #id zaten benzersiz bir alan yani tek old. için fetchone yeter fetchall diyip for a gerek yok


    for products in sonuc:
        print(f"id: {products[0]}model:{products[1]} fiyat: {products[2]}")
        
kayitGetir()

def IdkayitGetir(id):
    baglan = mysql.connector.connect(host="localhost", user="root", password="mysql2004", database="deneme")

    cursor = baglan.cursor()

    sql = "Select * from products where id=%s"

    params = (id,)

    cursor.execute(sql, params)

    sonuc = cursor.fetchone() 

    print(f"id: {sonuc[0]} model:{sonuc[1]} fiyat: {sonuc[2]}")


IdkayitGetir(4) # biz hangi değeri yazarsak o id deki değeri bize getirir
IdkayitGetir(1) 
IdkayitGetir(3) 