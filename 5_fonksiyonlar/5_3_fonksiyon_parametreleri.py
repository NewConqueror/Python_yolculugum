
def changename(n):
    n="ada"

name = "yiğit"
changename(name) 
print(name)   # değer gönderildiği için kendisi değişmez

def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"] 
change(sehirler)
print(sehirler) # listelerde adres ile gönderildiği için asıl değeri değişir

n = sehirler

n[0] = "trabzon"
print(sehirler) # n ile sehirlerin adreslerini eşitlediğimiz için birinde yaptığımız değişiklik diğerini de etkilicek

n = sehirler[:] # slicing parçalama işlemi yapıyoruz bu sefer adresi göndermek yerine sadece değerleri kopyaladık
n[0] = "kocaeli"

print(sehirler) # değerleri kopyaladığımız için sehirler değişmicek sadece değiştirdiğimiz n değişecek
                # print(sehirler) = ankara, izmir şeklinde olucak   n ise kocaeli izmir şeklinde

change(sehirler[:]) # bu şekilde değerleri yollamış olduk adresi değil onun için
print(sehirler) # değerleri yolladığımız için aynı şekilde kalıcak değişmeyecek 



def topla(a,b):
    return sum(a,b) # direkt python kütüphanesinde olan bir fonksiyon

print(topla(10,20))
print(topla(10,20,30)) # 2 parametre var biz 3  tane yolladığımız için hata verir bu hatayı düzeltmek için
                       # şöyle yapabiliriz

def topla(a,b,c=0,d=0,e=0):
    return sum(a,b,c,d,e) 
print(topla(10,20))
print(topla(10,20,30))
print(topla(10,20,30,40,5))

# en fazl 5 yolladık peki 6 tane istersek ne yapıcaz 


def topla(*parametreler): 
    print(parametreler) # bunu yaptığın zaman görüceksin ki bir liste şeklinde tutuyor tuple listesi
    print(parametreler[0])
    print(parametreler[2]) # liste olduğu için bunları yapabilirsin
    
    return sum( (parametreler) )

# ben sum fonksiyonu kullanmak istemiyorum kardeşim hay hay

def topla(*parametreler):
    print(type(parametreler)) # tuple listesi vericek
    sonuc = 0
    for n in parametreler:
        sonuc+=n

    return sonuc

# peki ya farklı tipte veriler yollasam  1.parametre adı 2.parametre yaşadığı yer 3.parametre maaş bilgisi
# şeklinde bir veri göndermek istediğim zaman ve bu verilerin sayısı belli değil istediğim kadar yollayabilicem
# örn 1.kullanıcı 3 tane 2.kullanıcı 5 tane özelliğini gönderebilicem

# bu şekilde bir fonk yazabilmek için gönderdiğimizin liste olması yeterli değil çünkü listeden gönderdiğim verinin
# hangi tipte bir veri olduğunu bilemem

#bu bilgileri dictionary kullanarak yapıyorduk işte name karşısında value şeklinde bir yapıydı bunu nasıl yapıcaz gör

                # dictionary veri tipi için 2 tane * işareti koyuyoruz  **sozluk de olabilirdi argumana takılma
def displayUser(**argumanlar):
    print(type(argumanlar))

    for key,value in argumanlar.items():
        print("{} is {}".format(key,value))

# bu şekilde farklı tipte ve farklı sayıda argümanları alabiliyoruz

displayUser(name = "fatih" , yas = 18 , şehir = "istanbul")
displayUser(name = "saliha" , yas = 12 , şehir = "trabzon", telefon = "537")
displayUser(name = "cemre" , yas = 19 , şehir = "istanbul", telefon = "538", email = "cemre@gmail.com")


def ortayaKarisik(a,b, *parametreler, **argumanlar):
    print(a)
    print(b)
    print(parametreler)
    print(argumanlar)


ortayaKarisik(10, 20, 30, 40, 50, key1 = "value1", key2 = "value2")

# bunu çalıştırdığımız zaman 10 un a ya 20 nin b ye sonra key1 değerine kadar olan 
# 30 40 50 değerinin parametreler listesinin içine atıldığını çıktının (30,40,50) old görebiliriz
# key1 value1 key2 value2 değerlerinin de dictionary içine atılıdığını görebiliriz
# dictionary nin çıktısı da böyle olur { "key1" = "value1", "key2" = "value2" } 