numbers = []
for x in range(10):
    numbers.append(x)  # böyle eklemek yerine

print(numbers)

numbers = [x for x in range(10)]  # böyle ekleyebilirsin ilginç bir kullanım gerçekten

print(numbers)

for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)    

numbers = [x*x for x in range(10) if (x%3==0)]
print(numbers)

mystring = "hello"

mylist = []

for letter in mystring:
    mylist.append(letter) # ikisi de aynı işe yarıyor
print(mylist)

mylist = [letter for letter in mystring]  # bu daha ilginç bir kullanım kod tasarrufu
print(mylist)

years = [1983,1999,2008,1956,1986]

ages = [2019-yil for yil in years]

print(ages)

sonuc = [x if (x%2==0) else "tek" for x in range(1,10)] 
# if sondaysa else e gerek yok ama if baştaysa else kullanmak zorundasın
print(sonuc)

result = []

for i in range(3):
    for j in range(3):
     result.append((i,j))

print(result)


numbers = [ (i,j,k) for i in range(3) for j in range(3) for k in range(3) ]
print(numbers)