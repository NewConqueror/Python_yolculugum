import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # şuan böyle 192.11.11.11  # server kiralarsak böyle bir değer vericek ona göre yazıcaz
    user = "root",
    password = "mysql2004"
)
 
# print(mydb) # bize mysql connection tipinde  bir nesne döndürecek

mycursor = mydb.cursor()       # bağlantıyı kurduk

#mycursor.execute("CREATE DATABASE mydatabase")  # mydatabase adında yeni bir database oluşturduk zaten varsa hata verir

#mycursor.execute("SHOW DATABASES") # bütün databaseleri bize listele göster dedik for döngüsüyle yaptık

# for x in mycursor:
#     print(x)


mydb = mysql.connector.connect(
    host = "localhost", # şuan böyle 192.11.11.11  # server kiralarsak böyle bir değer vericek ona göre yazıcaz
    user = "root",
    password = "mysql2004",
    database = "mydatabase"  # hangi database de işlem yapacağımızı söyledik
)

imlec = mydb.cursor()

imlec.execute("CREATE TABLE musteriler (ad VARCHAR(45), adres VARCHAR(45))") 

# musteriler adında bir tablo oluşturduk nerde mydatabase in altında çünkü bağlantıyı ona göre yaptık