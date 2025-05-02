def kare(sayi): return sayi**2  # bu şekilde de yazabiliriz sonuçta aynı şey 

numbers = [1,3,5,9] # her bir elemanın karesini alıp bir listeye atmak istiyorum
# nasıl yaparız her elemana ulaşırız for döngüsüyle kare ye yollayıp listeye ekleriz
# bunun yerine daha pratik olanı var map ile

sonuc = list( map(kare,numbers) ) # kullanacağımız fonksiyonun "sadece adı" ve dizinin ismi ile listeye çevirdik
# veya şöyle de kullanabiliriz

for item in map(kare,numbers): # sadece listeye çevirmek zorunda değil for döngüsü ile de olur
    print(item)

print(sonuc)

# def kare(sayi): return sayi**2 fonksiyonu ayrı bir yerde tanımlamak yerine şöyle yapabiliriz

sonuc = list( map( lambda sayi : sayi**2 ,numbers) ) 
# sadece burda 1 kere çalıştırılacak bir işlem her zaman ihtiyaç duymicam ismi olmayan bir fonk lambda 
# return e ihtiyaç duymadan karesini alabilirz
# aynı işe yarar sadece isimsiz bir fonk ile yaptık

# illa isimsiz olmak zorunda değil bir isim de verebiliyoruz

square = lambda sayi: sayi**2
sonuc = list( map( square,numbers) ) # hata vermez aynen çalışır 

# normal bir fonksiyon gibi de kullanabiliriz

a = square(5) 
print(a) # 25 sonucunu verir

# direkt te kullanabiliriz
# fonksiyon gibi de yapabiliriz sana kalmış

# diyelim ki ben bütün elemanlarda işlem yapmak istiyorum ama hepsi geri dönmesin filtrelemek istiyorum sadece çiftler mesela

def ciftmi(sayi): return sayi%2==0

sonuc = list( filter( ciftmi,numbers) ) # fonk tanımlayıp böyle de kullanabiliriz
sonuc = list( filter( lambda sayi: sayi%2==0, numbers)) # tanımlamadan böyle de yapabiliriz

# şöyle de olabilir 

ciftmi = lambda sayi: sayi%2==0

sonuc = list( filter( ciftmi,numbers) ) 

result = ciftmi(numbers[2]) # True ya da False değer döndürür
