# generator bellekte yer kaplamayan iterator üretiyor  bu ne anlama geliyor

def kup():
    sonuc = []

    for i in range(5):
        sonuc.append(i**3)
    return sonuc

print(kup) # ekrana bir liste yazdırılır ve dikkat edersen şu anda liste bellekte bir alan işgal ediyor

# eğer bu elemanlara tekrar ulaşma ihtiyacım olmayacaksa sadece ekranda göstermem gerekiyorsa bellekte bir yer
# işgal etmeye gerek yok 5 için sorun yok ama 500 bin olsa bellekte ciddi yer işgal eder gereksiz yere
# çünkü zaten bir daha ulaşmicam ihtiyacım olmayacak

# bunu için bellek üzerinde yer kaplamayan generator ı kullanabiliriz


def kup():
    
    for i in range(5):
        yield i**3     # yield burda bir değer üretiyor bu değeri bana gönderiyor ve gönderdikten sonra bu değer
#                        herhangi bir yerde saklanmıyor 2.defa ulaşmak istersem ulaşamam çünkü bir yerde tutulmuyor
#                        üretiliyor ve üretildiği anda da kullanılıyor
#                        yield ile ürettiğimiz şey iterator bir obje yani itarete edilebilen nesne

print(kup) # bize bir generator nesnesi gönderiyor bu fonksiyon

generator = kup() # bize iterate edilebilen yani üzerinde dolaşabileceğimiz bir iterator nesnesi gönderiyor

# üzerinde dolaşmak için bir iteratör oluşturmamız gerekiyor yani "generator aslında iterator bir nesne"

iterator = iter(generator)  # illa buna gerek yok çünkü kup() zaten iterator bir nesne döndürüyor bize

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) # ya da

iteratorüm = kup() # kup direkt iteratör bir nesne döndürdüğü için böyle de yapabiliriz
#                    ama böyle yaparsak bu iteratör olmadığından dolayı nesne olduğundan dolayı next ile kullanamayız
                    
for i in iteratorüm: # ama for ile kullanabiliriz çünkü for iteratör nesnesinden dolaşabileceği iteratörü kendi
    print(i)         # oluşturuyor

for i in kup(): # veya direkt böyle yapabiliriz çünkü kup() fonksiyonu iterator obje döndürüyor
    print(i)    # for da üzerinde dolaşmak için iterator objeden bir iteratör oluşturuyor
#               ne zaman generator üzerinden bilgi istersen yield o anda çalışıyor
#               o anda yield çalışır durdurulur tekrar istersen yine çalışır durdurulur böyle devam eder

# for ile kullanırsan zaten StopIteration gelene kadar bu işlem devam eder


# liste = [i**3 for i in range(5)] # bu şekilde yaparsan bu bir liste olur
# print(liste)                  

# gelen sonucu generator yapmak istiyorsan böyle normal parantez ile yazmalısın 
# liste = (i**3 for i in range(5)) 
# print(liste)                    # böylece gelen bir generator objesi olur


generator = (i**3 for i in range(5)) 
print(generator)                    # böylece gelen bir generator objesi olur

print(next(generator))
print(next(generator))
print(next(generator)) # ya da for döngüsü

for i in generator:
    print(i)