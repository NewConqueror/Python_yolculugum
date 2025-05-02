# global alan
x = "global x"

def fonksiyon():
    #lokal alan
    x = "lokal x"
    print(x)

fonksiyon()
print(x) 

# fonksiyon ve normalin alanları ayrı olduğu için değişkenler birbiri yerine  geçmez yani üstünde değişiklik yaparsan
# fonksiyonda yaptığın fonksiyonda kalır global ile lokal ayrıdır

# global
ad = "cinar"

def changname(isim):
    #lokal
    ad = isim
    print(ad)

changname("ada")
print(ad)


################

# bunu çözmek için yani fonksiyonda değiştirdiğimiz değer dışarıdaki değeri de değiştirsin istiyorsak
# global değişken diyerek lokal da yaptığımız değişkenlerin globali de değiştirmesine izin vermiş oluruz

name = "global string"

def selamlama():
    global name
    name = "cinar"

    def merhaba():
        print("merhaba "+ name)

    merhaba()

selamlama() 

# yine aynı şekilde dışarıdaki global x i fonk içinde değiştirdiğimizde normalde de değişsin istedik
# bu yüzden başına global ekledik ve lokaldeki değişiklik globaldekini de etkiledi

x = 50

def test():
    global x
    print(f"x: {x}")

    x=100
    print(f"değiştirilen x: {x}")

test()
print(x)
