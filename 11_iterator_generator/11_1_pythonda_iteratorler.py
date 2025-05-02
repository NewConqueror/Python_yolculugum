liste = [1,2,3,4,5]

for i in liste: # liste elemanı iterator bir obje iterator bir obje olduğu için for döngüsü ile gezebiliyoruz üstünde
    print(i)

print(dir(liste)) # bakarsak liste içinde __iter__ metoduna sahip olduğunu görürüz

# iterator bir obje üzerinde elemanları tek tek dolaşmak için iterator objeden bir iteratör oluşturmamız gerekiyor
# bir iteratör elemanlar üzerinde tek tek dolaşmamızı sağlar 
# for döngüsü bizim yerimize iterator bir objeden iteratör oluşturuyor o sayede geziyor

iteratör = iter(liste) # iter fonksiyonu listeden bir iteratör oluşturdu çünkü liste iterator bir obje
print(iteratör) # iteratör nesnesinin oluşturulduğunu görebiliriz

# bu şekilde elemanlar üstünde gezebilirsin
print(next(iteratör)) # 1
print(next(iteratör)) # 2
print(next(iteratör)) # 3
print(next(iteratör)) # 4
print(next(iteratör)) # 5
# print(next(iteratör)) # başka eleman olmadığı için StopIteration hatası alırız

for i in liste: # for un arkasında dönen hikaye bu  işte
    print(i)  

iteratörüm = iter(liste) # üzerinde gezmek için iterator objeden iter metodu ile iteratör oluştur

while True:            
    try:
        element = next(iteratörüm)      # sıradikini yaz yoksa döngüden çık
        print(element)
    except StopIteration:
        break

# peki aga bu kadar işlemi neden yapıyoruz for döngüsü ile zaten kolayca yapabiliyoruz
# iteratör ün bu şekilde oluşturulmasını neden bilme ihtiyacı duyuyoruz

# çünkü bir list gibi bir sınıfı kendimiz oluşturmak isteyebiliriz ve bu durumda iteratör kullanabiliriz


class sayilar:

    def __init__(self,bas,son):
        self.bas = bas
        self.son = son

    def __iter__(self):
        return self

    def __next__(self):
        if (self.bas <= self.son):
            x = self.bas
            self.bas+=1
            return x 
        else:
            raise StopIteration


listem = sayilar(10,20)
#                x = iter(listem) bu şekilde düşünebilirsin
for x in listem: # for çalışır çünkü listem bir iterator obje for da elemanları gezmek için bu iterator objeden
    print(x)     # bir iteratör oluşturuyor otomatik olarak 

# for olmadan ise aşağıdaki şekilde yapabiliriz

myiter = iter(listem)

while True:
    try:
        eleman = next(listem)
        print(eleman)
    except StopIteration:
        break



