import datetime

sonuc = dir(datetime) # date time datetime gibi alt sınıflar var sadece böyle yaparsak
sonuc = datetime.time # böyle bir kullanım yapmamız gerekir  ya da 
sonuc = datetime.date

from datetime import datetime
from datetime import time # alt sınıfları böyle de çağırabiliriz bütün datetime a gerek yok aq
from datetime import date

sonuc = dir(datetime) # now hour date gibi kullanabileceğimiz metotları gösterir

simdi = datetime.now() # şuanki saat ve tarih bilgisini getirir
simdi = datetime.today() # ikisi de aynı işi yapar
sonuc = simdi.year      # simdi bir datetime nesnesi olduğu için bu şekilde de yapabilirz
sonuc = simdi.month  
sonuc = simdi.day
sonuc = simdi.minute
sonuc = simdi.second
#                                                  simdi
sonuc = datetime.ctime(simdi) #ctime bir datetime nesnesi alıyor tarihi daha açıklayıcı şekilde söylüyor gün ay yil vs

sonuc = datetime.strftime(simdi, "%Y") # strftime da bir datetime nesnesi ve bir format bekler her biri ayrı bu yıl
sonuc = datetime.strftime(simdi, "%X") # sadece saat
sonuc = datetime.strftime(simdi, "%d") # sadece gün
sonuc = datetime.strftime(simdi, "%A") # sadece hangi gün pzt salı vs
sonuc = datetime.strftime(simdi, "%B") # sadece ay temmuz vs
sonuc = datetime.strftime(simdi, "%Y %B %A") # bu şekilde çoklu da kullanabilirsin yıl hangi ay hangi gün
# bu yazım şekillerine işte A ne B ne vs diye google a datetime python yazarak bulabilirsin


t = "10 kasım 1938"     #böyleyse split ile hallederiz ama ya böyle değilse bölünemeyecek durumdaysa
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)

t = "10 kasım 1938 saat 09:05:00"     # bu şekildeyse nasıl yapıcaz mesela 

dt = datetime.strptime(t, "%d %B %Y saat %H:%M:%S") #bir string vet sonra formatı belirle
result = dt.year # datetime nesnesi old için böyle de yapabiliriz artık

print(dt)


dogumgunu = datetime(2004,7,28,12,30,45) #sorunsuz şekilde atar 2004-7-28 12:30:45 diye

result = datetime.timestamp(dogumgunu) # datetime ı saniyeye çeviri çevirirken de 1970 ten şimdiye kadar aralıkta yapar

result = datetime.fromtimestamp(result) # saniyeyi tekrar datetime a çevirir

result = datetime.fromtimestamp(0) # neden 1970 bilgisayarların miladının bu olduğu söylenebilir


result = simdi - dogumgunu # 2 tarih arasındaki fark bulunur gün ve saat cinsinden

# bu obje timedelta objesi  zaman farkı nesnesi de diyebiliriz farklı bir class tan yani    

result = result.days  # zaman farkını gün cinsinden
result = result.seconds # saniye cinsinden
result = result.microseconds # mikrosaniye cinsinden döndürür

# ileri bir tarihi bulmak istiyorsak o zaman timdelta yı import etmemiz gerekiyor

from datetime import timedelta

sonuc = simdi + timedelta(days=10) # şimdiki tarihin üstüne 10 gün ekler

sonuc = simdi + timedelta(days=730, minutes=10) # şimdiki tarihin üstüne 730 gün 10 dakika ekledi

# aynı şekilde çıkarma da yapabiliyoruz

sonuc = simdi - timedelta(days=10) # şimdiki tarihten 10 gün çıkartacak

# datetime objesi olması bir sürü avantaj sağlar
# ya da string bir ifadeyi datetime nesnesine çeviriyor olmak fayda sağlar

print(sonuc) 

