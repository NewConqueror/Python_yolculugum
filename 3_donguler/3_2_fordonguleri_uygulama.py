sayilar = [1,3,5,7,9,12,19,21]

# hangi sayılar 3 ün katı

for i in sayilar:
    if(i%3==0):
        print(i)

# sayıların toplamı kaç
topla=0
for i in sayilar:
    topla+=i

print("toplam: ",topla)

# tek sayıların karesini alın
for i in sayilar:
    if(i % 2!=0):
        print(i**2)


sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# şehirlerden hangileri en fazla 5 karakterlidir

for i in sehirler:
    if(len(i)<=5):
        print(i)


urunler = [ # dictionary veri tipinde
    {'model':'samsung s6', 'fiyat': '3000'},
    {'model':'samsung s7', 'fiyat': '4000'},
    {'model':'samsung s8', 'fiyat': '5000'},
    {'model':'samsung s9', 'fiyat': '6000'},
    {'model':'samsung s10','fiyat': '7000'}
]

# ürünlerin fiyatları toplamı nedir

#for urun in urunler:
#print(urun) 
# {'model: ': 'samsung s6', 'fiyat: ': '3000'} {'model: ': 'samsung s7', 'fiyat: ': '4000'}
#{'model: ': 'samsung s8', 'fiyat: ': '5000'}{'model: ': 'samsung s9', 'fiyat: ': '6000'}{'model: ': 'samsung s10', 'fiyat: ': '7000'}
# direkt urun dersek bu şekilde yazdırır

toplam = 0
for urun in urunler:
    print(urun['fiyat'])
    toplam+=int(urun['fiyat'])

print("toplam ürün fiyatı: ",toplam)

# ürünlerden fiyatı en fazla 5000 olanları gösteriniz

for urun in urunler:
    if(int(urun['fiyat'])<=5000):
        print(urun['model'])

