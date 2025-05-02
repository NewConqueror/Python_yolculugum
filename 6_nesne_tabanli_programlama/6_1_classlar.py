# class - sınıf

# # direkt böyle oluşturamıyoruz ya attributes ya da method eklemek zorundayız ama bunları yapmadan da bir yolu var
# a=20
# if a >10:
#     pass 
# class Person:
#     pass # pass i kullanarak attributes veya method tanımlamak zorunda olmadan class oluşturabiliriz
#     # attributes
#     # methods
# a=20
# if a >10:
#     pass  # burda da gördüğümüz gibi eğer içini boş bırakmak istiyorsak pass kullanırız


class Person:
    pass

    # class attributes # her zaman kullanmayacağın özellikleri class attributes olarak tanımlayabilirsin
    adres = "no information"

    # constructor ( yapıcı metot)
    # def __init__(self) -> None: # direkt tab layınca böyle geldi 
    #     pass

    def __init__(self,ad,yil): # constructor a olması zorunlu şeyleri yaz

    #def __init__(this,ad,yil): # self olmak zorunda değil this de yapabilirsin
    
    # object attributes
        self.ad = "fatih"
        self.yil = 2004
        print("init metodu calisti")

        # this.ad = "fatih"
        # this.yil = 2004

    # methods



# object (instance)

p1 = Person("fatih",1939) # self this vs kendiliğinden geliyor senin ayrıca yazmana gerek yok diğerlerini yaz
p2 = Person(ad ="saliha", yil =2012) # böyle de yapabilirsin 

# updating
p1.name = "ali"
p1.yil = 1945
p1.adres = "istanbul"  # direkt böyle yapabilirsin dikkat edersen constructor a adresi yazmadık ama kullandık
                       # hep kullanmayacağın değişkenleri böyle yap


 # accessing object attributes
print(f"p1 : ad {p1.ad} year: {p1.yil} adres: {p1.adres} ")
print(f"p2 : ad {p2.ad} year: {p2.yil} adres: {p2.adres}")

print(p1)
print(p2) # adres yazdırırlar type(p1) yaparsan da class person yazdığını görürsün