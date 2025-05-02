
class Person:
    pass

    # class attributes7
    adres = "no information"

    # constructor ( yapıcı metot)
    def __init__(self,ad,yil): # constructor a olması zorunlu şeyleri yaz

    
    # object attributes
        self.ad = ad
        self.yil = yil
        print("init metodu calisti")

    # methods
    def giris(self):  # bunlarda böyle kendisi için self i vermen gerekiyor
        print(f"merhabalar ben {self.ad}")
    
    def yashesapla(self):
        return 2023 - self.yil

# object (instance)

p1 = Person("fatih",1939) 
p2 = Person(ad ="saliha", yil =2012)

p1.giris()

print(f"adim: {p1.ad} ve yasim: {p1.yashesapla()} ")
print(f"adim: {p2.ad} ve yasim: {p2.yashesapla()} ")





class daire:
    # class object attributes
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap  # aynı olmak zorunda değil self.r = yaricap da diyebilirdik

    # methods

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)
    

c1 = daire(4)
c2 = daire()

print(f"cevre: {c1.cevreHesapla()} alan: {c1.alanHesapla()}")
print(f"cevre: {c2.cevreHesapla()} alan: {c2.alanHesapla()}")
         



