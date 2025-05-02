# 1 - "bmw,mercedes,opel,mazda" elemanlarına sahip bir liste oluşturunuz
arabalar = ["bmw","mercedes","opel","mazda"]

# 2 - liste kaç elemanlıdır
uzunluk = len(arabalar)
print(uzunluk)

# 3 - listenin ilk ve son elemanı nedir

print(arabalar[0])
print(arabalar[-1])  # sondaki elemana böyle de erişebilirsin arabalar[uzunluk-1] de diyebilirsin

# 4 - mazda ile toyotanın yerini değiştirin

arabalar[-1] = 'toyota'
print(arabalar)

# 5 - mercedes listenin bir elemani midir

varmi = 'mercedes' in arabalar # arabalardaki bütün elemanları döner foreach gibi  mercedes varsa True yoksa False döndürür

# 6 - listenin -2 indiksindeki değer nedir

print(arabalar[-2])

# 7 - listenin ilk 3 elemanını alın

arabalar = arabalar[0:3]  #tıpkı stringlerde olduğu gibi 0. indisten 3.indise kadar alıcak arabalar = arabalar[:3]
print(arabalar)

# 8 - listenin son 2 elemanı yerine "toyota" ve "renault" değerlerini ekleyin
 
arabalar[-2:] = ["toyota","renault"]  # -2. indisten sona sırasıyla toyota ve renault u ata
print(arabalar)

# 9 - listenin üzerine "audi" ve "nissan" değerlerini ekleyin

arabalar = arabalar + ["audi","nissan"]
print(arabalar)

# 10 - listenin son elemanını silin

del arabalar[-1]
sonuc = arabalar
print(sonuc)
# 11 - liste elemanlarını tersten yazdırınız

print(arabalar[::-1])

# 12 - aşağıdaki verileri bir liste içinde saklayınız

# studentA: yiğit bilgi 2010, (70,60,70)
# studentB: sena turan  1999, (80,80,70)
# studentC: ahmet turan 1998, (80,70,90)

studentA = ["yiğit","bilgi",2010,[70,60,70]]
studentB = ["sena","turan" ,1999,[80,80,70]]
studentC = ["ahmet","turan",1998,[80,70,90]]

# 13 - liste elemanlarını ekrana yazdırınız

print(studentA[0]) # yiğit
print(studentB[1]) # turan
print(studentC[3])  # bunda bir dizi görücez [3][0],[3][1],[3][2] sini görücez

print(f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3} dir")