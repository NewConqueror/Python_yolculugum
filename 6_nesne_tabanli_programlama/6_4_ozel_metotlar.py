mylist = [1,2,3]
mystring = "my string"

print(type(mylist))
print(len(mylist))

print(type(mystring))
print(len(mystring))



# class film():
#     pass

#f = film()
#print(type(f))
#print(len(f))  # burada hata verip len fonksiyonunun film sınıfı için tanımlı olmadığını söylicek ama mylist veya
#               mystring için böyle bir şey demicek çünkü mylist liste tipinde bir SINIF 
#               mystring str tipinde bir SINIF len fonksiyonu bunlar için override edilmiş gibi düşünebilirsin

"""
burada hata verip len fonksiyonunun film sınıfı için tanımlı olmadığını söylicek ama mylist veya
mystring için böyle bir şey demicek çünkü mylist liste tipinde bir SINIF 
mystring str tipinde bir SINIF len fonksiyonu bunlar için override edilmiş gibi düşünebilirsin

"""

# class film():
#     def __init__(self,adi,yonetmeni,suresi):
#         self.ad=adi
#         self.yonetmen=yonetmeni
#         self.sure=suresi
#         print("film nesnesi oluşturuldu")

# f = film("oppenheimer","nolan","3 saat")

# print(str(mylist))
# print(str(f))      # biz kendimiz str yi tanımlayabiliriz zaten arka planda öyle oluyor7
                    # len metodu içinde aynı şey geçerli str için ayrı liste için ayrı tanımlı tanımlayalım



class film():
    def __init__(self,adi,yonetmeni,suresi):
        self.ad=adi
        self.yonetmen=yonetmeni
        self.sure=suresi
        print("film nesnesi oluşturuldu")

    def __str__(self):
        return (f"{self.ad} adlı filmi {self.yonetmen} adlı kişi yönetmiştir")
    
    def __len__(self):
        return self.sure  # int değer döndürmek zorunda len metodu
    
    def __del__(self):
        print("film nesnesi silindi")

f = film("oppenheimer","nolan",3)
print(str(f))
print(len(f))

# del f aynı şekilde del metodunu da tanımlayabiliriz kendimize göre 

# google a python special method list yazarsan kalan çoğunu da görebilirsin