import mysql.connector

def getproducts():
    
    bağlanti = mysql.connector.connect(host="localhost",user="root",password="mysql2004",database="deneme")
    imlec = bağlanti.cursor()

    sql = "select * from products"   # bütün products bilgileri gelir categoriesid dahil 1 2 şeklinde gelir
    sql = "select * from categories"  # bütün kategori bilgileri gelir
    sql = "select * from products inner join categories on categories.id=products.categoryid"
# categories in içindeki id ile products ın içindeki categoryid birbirine eşitse o kayıtları bize getirir
# product ın yanına categories i eklenmiş görürüz
    
    sql = "select products.ad,products.fiyat,categories.ad from products inner join categories on categories.id=products.categoryid"
#  products tan ad ve fiyat bilgisi gelir categories ten sadece ad bilgisi gelir id gelmez

    sql = "select products.ad,products.fiyat,categories.ad from products inner join categories on categories.id=products.categoryid where categories.ad='telefon'"
# products tan ad ve fiyat bilgisi gelir categories ten sadece ad bilgisi telefon olanlar gelir bilgisayar gelmez
   
    sql = "select products.ad,products.fiyat,categories.ad from products inner join categories on categories.id=products.categoryid where products.ad='samsung s10'"
# products tan ad ve fiyat bilgisi gelir categories ten sadece ad bilgisi samsung s10 olanlar gelir
    
    sql = "select p.ad,p.fiyat,c.ad from products as p inner join categories as c on c.id=p.categoryid where p.ad='samsung s10'"

    imlec.execute(sql)
    
    try:
        sonuc = imlec.fetchall() 

        for product in sonuc:
            print(product)

    except mysql.connector.Error as hata:
        print("hata: ",hata)

    finally:
        bağlanti.close()


getproducts()