import mysql.connector

baglanti = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="mysql2004",
    database = "okul"     # 10. ve 12. satırdan sonra ekledik yazdırdık var olduğunu görüp ekledik yani
    )

imlec = baglanti.cursor()

imlec.execute("SHOW DATABASES")

for i in imlec:
    print(i)



