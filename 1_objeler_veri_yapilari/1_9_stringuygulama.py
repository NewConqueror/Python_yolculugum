website = "http://www.fatihyeni.com"
course = "python kursu: baştan sona programlama (40 saat)"

# 1 course karakter dizisinde kaç karakter bulunmaktadır
uzunluk = len(course)

# 2 website içindeki www karakterlerini alın
print(website[7:10])

# 3 website içinden com karakterlerini alın
print(website[-3: ]) # bu da bir yöntem hoca şöyle yapmış website[22:25] benimki daha acayip hehe  
website[uzunluk-3: uzunluk]  # yukarıdaki ile aynı işi yapıyor

# 4 course içinden ilk 15 ve son 15 karakteri al
ilk15 = course[:15] # course[0:15]
son15 = course[-15:] # course[-15:uzunluk]

# 5 course ifadesindeki karakterleri tersten yazdırın
print(course[::-1]) # course[::]bütün her şeyi alır course[:: 2] dersem 2 şer 2 şer yazdırır ters yazdırması için -1 dedik 1 deseydik normal olurdu ters -1

ad,soyad,yas,job = "Bora","Yılmaz",32,"Mühendis"

# 6 yukarıda verilenler ile ekrana aşağıdakini yazdırın
# "benim adım Bora Yılmaz Yaşım 32 ve mesleğim mühendis."

print(f"benim adım {ad} {soyad}  Yaşım {yas} ve mesleğim {job}")
print("benim adım {} {}  Yaşım {} ve mesleğim {}".format(ad,soyad,yas,job))
print("benim adım {0} {1}  Yaşım {2} ve mesleğim {3}".format(ad,soyad,yas,job))
# hepsi aynı işi yapar

# 7 hello world ifadesindeki w yi W ile değiştirin

s="hello world"

s= s[0:6] + 'W' + s[-4:] # böyle parçalayarak yapıyormuşuz

# s.replace('w','W') bu da olur ama bunu daha sonra görücez
print(s)

# 8 abc ifadesini yan yana 3 defa yazdırın

strr = "abc" * 3  # böyle ilginç bir kullanım da varmış direkt abcabcabc diye yazıyor
print(strr)