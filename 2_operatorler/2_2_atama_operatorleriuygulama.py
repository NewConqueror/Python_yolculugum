x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1 kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# sayi1 = input("1. sayiyi giriniz: ")
# sayi2 = input("2. sayiyi giriniz: ")
# sonuc = ( int(sayi1)*int(sayi2) ) - (x+y+z) 
# 1.yol string olarak al int e çevir öyle işlem yap

sayi1 = int(input("1. sayiyi giriniz: "))
sayi2 = int(input("2. sayiyi giriniz: "))
# bu da 2.yol direkt int olarak al 
sonuc = ( sayi1*sayi2 ) - (x+y+z) 
print(sonuc)

# 2 y nin x e kalansız bölümünü hesaplayınız

sonuc = y //x
print(sonuc)

# 3 (x,y,z) toplamının mod 3 ü nedir

sonuc = (x+y+z)%3
print(sonuc)

# 4 y nin x.kuvvetini hesaplayınız

sonuc = y**x
print(sonuc)

# 5 x, *y, z = numbers işlemine göre z nin küpü kaçtır

x, *y,z = numbers
sonuc = z**3
print(sonuc)

# 6 x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır

x, *y, z = numbers

sonuc = y[0] + y[1] + y[2]
print(sonuc)
