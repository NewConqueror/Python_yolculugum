import os

sonuc = dir(os) # içinde bir sürü sınıf fonksiyon vs var biz en çok kullanılanlara bakıcaz kalanı doküman

# genellikle os modülü işletim sistemi ile ilgili bir bilgi sunar işletim sistemiyle alakalı bir bilgi talebi
# klasörler hakkında oluştur sil path sınıfı üzerinden de yapabilirsin bunları görelim

sonuc = os.name # işletim sistemini söyler nt windows demek

sonuc = os.getcwd() # dosyamızın hangi klasör altında bulunduğunu bize söyler
os.mkdir("newdirectory") # yeni klasör oluşturur ama bizim bulunduğumuz dizinde yani

os.chdir("C:\\") # bizi C:\\ dizinine götürdü şuan buradayız eğer bu şekilde dizin değiştirebiliriz
os.mkdir("newdirectory") # dersek C:\\ dizini altında klasörü oluşturur bulunduğumuz dizinde klasör oluşturabiliriz

os.chdir("..") # bir üst dizine geçeriz
os.chdir("../..") # bu şekilde yaparsak 2 kere üst dizine geçmiş oluruz 2 kere yukarıdakini de yapabilirdik tabi

os.makedirs("yeniklasör/newdirectory2") # makedirs komutu iç içe dizin oluşturmayı sağlar 
#os.makedirs("C:\\yeniklasör/newdirectory2")böylede oluşturulabilir şuan yeniklasör altında newdirectory2diye bir klasör var


sonuc = os.listdir() # bulunduğumuz dizin altındaki klasör ve dosyaları bize listeler
sonuc = os.listdir("C:\\") # söylediğimiz C:\\ dizini altındaki klasör ve dosyaları bize listeler

for dosya in os.listdir(): 
    if dosya.endswith(".py"):  # mesela bu işe yarar dizindeki bütün .py uzantılı dosyaları bize gösterir
        print(dosya) 

sonuc = os.stat("ders68_pythonda_os_modülü.py") # dosya hakkında bazı bilgiler verir ama sana anlamsız gelicek
# st_size = 1524  st_atime = 3155641 gibi şeyler bunu anlamlandırmak için datetime modülü kullanıcaz

import datetime

sonuc = sonuc.st_size #dosya boyutunu byte cinsinden verir 1024 e bölersen kB cinsinden bulursun
# sadece sonuc.st_ctime saniye cinsinden anlamsız döndürür ctime dosyanın oluşturulma zamanını bize söyler
sonuc = datetime.datetime.fromtimestamp(sonuc.st_ctime) # bunu fromtimestamp ile anlamlı hale çevirdik

sonuc = datetime.datetime.fromtimestamp(sonuc.st_atime) # dosyaya son erişilme tarihini verir

sonuc = datetime.datetime.fromtimestamp(sonuc.st_mtime) # dosyanın değiştirilme tarihini verir  

os.system("notepad.exe") # bunu çalıştırdığımızda not defteri çalışır böyle şeyleri de çalıştırabiliriz os sayesinde

os.rename("newdirectory","fatihyeniklasör") # newdirectory ismini fatihyeniklasör olarak değiştirir

os.rmdir("yeniklasör") #yeniklasör adlı klasörü siler removedirectory bu alt klasör olmadığı zaman kullanılır sadece bu
                                                         
os.removedirs("yeniklasör/yenikklasör") # bu da alt dizinler olduğu zaman kullanılır yk yi ve altındaki ykk yi siler


# path path daha çok uzantılar üzerinde işlem yapar uzantı değiştirme isim değiştirme vs os nin bir sınıfı

sonuc = os.path.abspath("ders68_pythonda_os_modülü.py") # bu dosyanın tam konumunu yolunu bize verir

sonuc = os.path.dirname("C:/Users/Halime/OneDrive/Masaüstü/python/python_dersleri/ders68_pythonda_os_modülü.py")
# tam konumu verilen bir dosyanın dizin ismini alıyoruz 
# bize dosyanın tam yolunu vermiş oldu e az önce öğrendim zaten bir daha niye amele gibi kullaniyim
# aslında ikisini birleştirmen gerekiyor
#                                                   tam konumu buluyor ordan da dizin ismini veriyor
sonuc = os.path.dirname(os.path.abspath("ders68_pythonda_os_modülü.py")) 


sonuc = os.path.exists("ders68_pythonda_os_modülü.py") # aradığı konumda dosya var mı yokmu onu söyler şuan bizimkinde
# True döndürür

sonuc = os.path.exists("C:/Users/Halime/OneDrive/Masaüstü/python/python_dersleri/ders68_pythonda_os_modülüüü.py")
# böyle bir şey olmadığı için false döndürür

sonuc = os.path.exists("C:/Users/Halime/OneDrive/Masaüstü/python/python_dersleri") # True
sonuc = os.path.exists("C:/Users/Halime/OneDrive/Masaüstü/python/python_derslerii") # False
# sadece dosya değil klasör de sorgulayabiliriz

sonuc = os.path.isdir("C:/Users/Halime/OneDrive/Masaüstü") # klasör mü değil mi onu söyler exist gibi True
sonuc = os.path.isdir("C:/Users/Halime/OneDrive/Masaüstü/python/python_dersleri") # dosya old için False der
#                                                                                  False çünkü bir klasör
sonuc = os.path.isfile("C:/Users/Halime/OneDrive/Masaüstü/python/python_dersleri") # dosya mı değil mi onu söyler
sonuc = os.path.isfile("C:/Users/Halime/OneDrive/Masaüstü/python/python_dersleri/ders68_pythonda_os_modülü.py")
# True veya sonuc = os.path.isfile("ders68_pythonda_os_modülü.py") bu da olur belki ??

sonuc = os.path.join("C://","deneme","deneme2") # yazdığımız yolları birleştirmek için kullanılır C:\\d\d2 diye

sonuc = os.path.split("C://deneme/deneme2") # yazdığımız yolları ayırmak için kullanılır liste şeklinde olur
#                                             yani ('C:\\', 'deneme') şeklinde olur

sonuc = os.path.splitext("ders68_pythonda_os_modülü.py") # ismi ve uzantıyı ayırır yine liste şeklinde
#                                                         ( 'ders68_pythonda_os_modülü', '.py' )
dosyaadi = sonuc[0]
uzanti = sonuc[1]
print(sonuc)