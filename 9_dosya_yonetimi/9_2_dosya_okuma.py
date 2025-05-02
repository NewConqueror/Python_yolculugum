# dosya = open("newfile.txt") # açma modu vermezsek default olarak okuma modunda gelir ama sen yine yaz
# print(dosya) # burda da görebilirsin 

# try:
#     file = open("newfile2.txt")
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     file.close()
#     print("dosya kapandı")

dosya = open("newfile.txt","r",encoding= "utf-8")

# for döngüsü ile olur

# for i in dosya:
#     print(i) # print her okuduğu satırdan sonra bir satır boşluk bırakır
# fatih

# sadık

# saliha

# bu şekilde yazar bunu engellemek için

# for i in dosya:
#     print(i,end="")
# fatih
# sadık
# saliha 
# bu şekilde yazar

# read() fonksiyonu ile okuyabilirsin ister komple ister belli kısmı

# oku =dosya.read()
# print("içerik 1")
# print(oku)  # read fonksiyonunu kullanarak yazdırırsan printle boşluk bırakmıyor

# dosya = open("newfile.txt","r",encoding= "utf-8") #böyle yaparsak imleç tekrar başa gelir ve okur

# oku2 = dosya.read() 
# print("içerik 2")
# print(oku2)
# imleç 1 de okudu sona geldi dosyayı kapatmadığımız için hala sonda o yüzden oku2 de bir şey yazmadı


# content = dosya.read(5) # sadece baştan imleç başta olduğu için 5 karakter okur
# print(content)  
# content = dosya.read(3) # imleçin kaldığı yerden okumaya devam eder 3 karakter okur
# print(content)
# content = dosya.read(3) # imleçin kaldığı yerden okumaya devam eder 3 karakter okur
# print(content)

# dosya.close()

# readline fonksiyonu satır satır okur while ile kullanırsın büyük ihtimal

# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())  # böyle yaparsan print yüzünden boşluklu okur

print(dosya.readline(),end="")
print(dosya.readline(),end="") # böyle normal okur
print(dosya.readline(),end="")
print(dosya.readline(),end="") # sondaki boşluğu sildiğimiz için burda bir şey yazmaz
print(dosya.readline()) # boşluk ekler print yüzünden
print(dosya.readline()) # böyle yaparsak boşluk okur

# readlines() foksiyonu ile okuyabilirsin direkt bir liste oluşturur ve her okuduğu dizinin bir elemanı olur

liste = dosya.readlines()

print(liste[0])
print(liste[1])
print(liste[2])