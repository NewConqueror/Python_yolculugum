username = "fatihyeni"
password = "1234"

# isLoggedin = (username=="fatihyeni") and (password=="1234")

# if isLoggedin:
#     print("hoşgeldiniz")

if (username == "fatihyeni"):
    if(password == "1234"):
        print("hoşgeldiniz")
    else:
        print("parola yanlis")
else:
    print("kullanici adi yanlis") # expected indented block print i öne çek demek ilginç


x = int(input("x: "))
y = int(input("y: "))

if x>y:
    print("x y denbüyüktür")
elif x==y:
    print("x y ye eşittir")
else:
    print("x y den küçüktür")

sayi = int(input("sayi: "))

if sayi>0:
    print("sayi pozitif")
elif sayi<0:
    print("sayi negatif")
else:
    print("sayi 0 a eşittir")


