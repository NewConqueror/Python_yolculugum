website = "http://www.fatihyeni.com"
course = "python kursu: baştan sona programlama (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin
sonuc = ' Hello World '.strip() # baştaki ve sondaki boşlukları siliyor
sonuc = ' Hello World '.lstrip() # sadece soldaki boşluk
sonuc = ' Hello World '.rstrip() # sadece sağdaki boşluk

#sonuc = website.lstrip('htp/:') # website karakter dizisi içinden bunları sil demiş olduk

# 2- website içindeki fatihyeni bilgisi haricindeki her karakteri silin

sonuc2 = 'www.fatihyeni.com'.strip('w.omc')

# 3 - course un içindeki her şeyi küçük harf yapın

course = course.lower()

# 4 - website içinde kaç tane a vardır (count('a'))

sonuc3 = website.count('a')  # a kaç kere geçiyor 
sonuc3 = website.count('www') # www kaç kere geçiyor 1
sonuc3 = website.count('www',0,10) # www kaç kere geçiyor 0. ile 10. index arasında bakıyor eğer o aralıkta yoksa yok kabul ediyor
# 5 - website www ile başlayıp com ile bitiyor mu 

basla = website.startswith("www") # www ile mi başlıyor hayır False döndürür
bitir = website.endswith("com")  # com ile mi bitiyor evet True döndürür

# 6 - website içinde .com ifadesi var mı

varmi = website.find(".com")  # .com var mı varsa index numarası yoksa -1
varmi = website.find(".com",0,10)  #.com 0. ile 10. index arasında var mı varsa index no yoksa -1

sonuc4 = course.find("python") # başta var 0 döndürür
sonuc4 = course.rfind("python") # aramaya sağdan yani sondan başlar bulduğu ilk python un index numarasını döndürür

sonuc4= website.index('com') # find ile aynı işi yapar index numarası döndürür
sonuc4= website.rindex('com') # aramaya sağdan başlar
sonuc4= website.rindex('comm') # find dan ayrılan farkı şu eğer yoksa find gibi -1 değil hata döndürür find dan farkı HATA döndürmesi

# 7 - course içindeki karakterlerin hepsi alfabetik mi  (isalpha,isdigit)

sonuc5 = course.isalpha() # course karakter dizisi alfabetik mi sadece harfler mi var hayır False değer döndürür
sonuc5 = 'hello'.isalpha() # hello alfabetik mi evet sadece harfler var True değer döndürür
sonuc5 = course.isdigit() # course karakter dizisi sadece sayılardan mı oluşuyor hayır False döndürür
sonuc5 = '123'.isdigit() # 123 sadece sayılardan mı oluşuyor evet True döndürür


# 8 - Contents ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz

s ='Contents'.center(50,'*') # ortalayacak şekilde sağa ve sola eşit * ekler
s ='Contents'.ljust(50,'*') # sola yaslı şekilde yazar * ları sağa ekler
s ='Contents'.rjust(50,'*') # sağa yaslı şekilde yazar * ları sola ekler

# 9 - course karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin

sonuc6 = course.replace(" ", '-') 
sonuc6 = course.replace(" ", '-',5) # sadece 5 tane karakteri değiştirir
sonuc6 = course.replace(" ", '') #bütün boşlukları siler 

# 10- Hello World karakter dizisinin World ifadesini There olarak değiştirin

sonuc7 = 'Hello World'.replace("World","There")

# 11 - course karakter dizisini boşluk karakterlerine göre ayırın

course = course.split(' ') #boşluk karakterlerine göre ayırıp her bir elemanı dizi içerisine attık 

# print(course[2])
# print(course[5]) vs vs
