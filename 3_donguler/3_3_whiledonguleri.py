# 1 den 100 e kadar

x=1

while x<=100:
    if( x%2==0):
        print(f"sayi çift {x}")
    else:
        print(f"sayi tek {x}")
    x+=1 # while içi else dışı


name = "" # False demek boş ad False

while not name.strip(): # "" False olduğu için not False yani True değerini döndürür boş olduğu sürece
    # strip ekledik ki boşluk karakterini yazmasın veya isim sayıp döngüyü sonlandırmasın
    name = input("isminiz: ")

print(f"merhaba {name}")  
