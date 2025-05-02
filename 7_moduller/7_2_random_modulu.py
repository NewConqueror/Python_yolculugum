import random

#sonuc = dir(random)   # kullanılabilecek bütün fonksiyonları gösterir
#sonuc = help(random) # bütün fonksiyonların nasıl kullanılacağını açıklar gösterir

sonuc = random.random()  # default olarak 0.0 ile 1.0 arasında sayılar döndürür

sonuc = random.uniform(10,100)  # 10 ile 100 arasında sayılar döndürür ama yine ondalıklı yani 80.856564 gibi
sonuc = int( random.uniform(10,100) ) # ondalıklıyı almayıp int a çevirdik 80

sonuc = random.randint(1,100) # 1 ile 100 arasında int sayılar döndürür

names = ["fatih","cemre","saliha","halime"]

sonuc = names[random.randint(0, len(names)-1)] # range hatası almadan rastgele bir eleman seçmek için böyle yaptık

sonuc = random.choice(names) #yukarıdaki gibi uğraşmak yerine bu fonksiyon direk bizim yerimize rastgele bir eleman seçiyor

selam = "merhabalar arkadaşlar"

sonuc = random.choice(selam) # karakter dizisi old için m h r a gibi elemanlar döndürür

listem = list(range(10)) # 0 dan 10 a kadar elemanları listeye çevirip listem değişkenine atar
#                          ama sıralı şekilde yapar 0 1 2 3 4 5 6 7 8 9 10 diye
random.shuffle(listem) # listeyi rastgele bir şekilde karıştırı [6, 5, 9, 0, 2, 8, 1, 7, 3, 4] bu çıktıyı verdi
#                       bir daha çalıştırsan daha farklı sonuç alırsın tabii ki
print(listem)

liste = range(100)

sonuc = random.sample(liste, 3) # belirttiğin liste içinden belirttiğin sayıda elemanı rastgele şekilde seçer

sonuc = random.sample(names, 2) # names ten rastgele 2 tane eleman seçer cemre ve halime mesela vs