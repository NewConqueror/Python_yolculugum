numbers = [1,2,3,4,5]

for sayi in numbers:
    print(sayi)

names = ["fatih","saliha","cemre"]

for ad in names:
    print(f"benim adım: {ad}")

name = "fatih yeni"

for c in name:
    print(c)  # stringler karakter dizisi old için f a t i h diye görürüz

tuple = (1,2,3,4,5)

for t in tuple:
    print(t)

tuple = [(1,2),(3,4),(5,7)]

for a,b in tuple:
 print(a,b) # sadece a yı yazdırırsak 1 3 5 sadece b yi yazdırırsak 2 4 7  a,b diyince 1 2 3 4 5 7) diye yazılır

d = {"k1":1, "k2":2, "k3":3}

for item in d:
   print(item) # sadece key değerlerini yazar value değerlerini yazmaz

for item in d.items():
    print(item) # bu şekilde yazarsak  ('k1', 1)\n ('k2', 2)\n ('k3', 3) bu şekilde yazar

for key,value in d.items():
   print(key,value)     # k1 1 \n k2 2 \n k3 3 bu şekilde yazar sadece key k1 k2 k3 sadece value 1 2 3 yazar
