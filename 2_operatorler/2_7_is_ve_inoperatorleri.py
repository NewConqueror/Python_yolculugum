# identity operatörü: is

x = y = [1,2,3]
z = [1,2,3]

print(x==y) # böyle yaparsak değerlere bakıyor o yüzden bunu True döndürür
print(x==z) # değerler aynı olduğu için 1,2,3 True döndürür

print(x is y) # bu şekilde referans olarak yani adres değerlerine bakıyor aynı olduğu için True döndürür
print(x is z) # değerlere değil adrese baktığı için ve tanımlarken farklı adreslerle tanımladığımız için
              # False değer döndürür

x = [1,2,3]
y = [2,4]

del x[2]
y[1] = 1
y.reverse()

print(x==y) # değerlere baktığı için ve değerler aynı olduğu için True döndürür

print(x is y) # adrese baktığı ve adresler farklı olduğu için False döndürür
print(x is not y) # adrese baktığı ve adresler farklı olduğu için True döndürür böyle bir kullanım da var


# Membership operatörü: in

x = ["elma","muz"]

print("muz" in x) # muz x in bir elemanı mı x in içinde mi True döndürür

name = "cinar"
print("a" in name) # stringler karakter dizisi olduğu için karakter karakter bakar a name değişkeni içinde var mı
                   # var olduğu için True döndürür
print("a" not in name) # bu da "a" name in içinde yoksa True döndürür var olduğu için False döndürecek