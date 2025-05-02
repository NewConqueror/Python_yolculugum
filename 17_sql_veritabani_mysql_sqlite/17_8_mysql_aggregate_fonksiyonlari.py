import mysql.connector

def getproductInfo():
    
    bağlanti = mysql.connector.connect(host="localhost",user="root",password="mysql2004",database="deneme")

    imlec = bağlanti.cursor()

    sql = "SELECT COUNT(*)FROM products"  #kaç tane kayıt olduğunu bize söyler 5 satır sayısını sayar name desen de aynı 
    sql = "SELECT AVG(fiyat) FROM products"  # fiyat alanının ortalamasını alır
    sql = "SELECT SUM(fiyat) FROM products"  # fiyat alanını komple toplar
    sql = "SELECT MAX(fiyat) FROM products"  # maximum fiyatı bize getirir
    sql = "SELECT MIN(fiyat) FROM products"  # minimum fiyatı bize getirir
    sql = "SELECT ad FROM products WHERE fiyat= (SELECT MAX(fiyat)FROM products)" #fiyat=60000 yazmamla aynı şey adını bize getirir

    imlec.execute(sql)

    sonuc = imlec.fetchall() 
        
    print(f"sonuc: {sonuc[0]}")  # fetchall yani liste tipinde old. için [0] ı yazmamız gerekiyor ya da for döngüsü


getproductInfo()