import numpy as np
# 1
dizi = np.array([10,15,30,45,60])
# 2
dizi =np.arange(5,15)
# #3
dizi = np.arange(50,100,5)
# #4
dizi = np.zeros(10)
# #5
dizi = np.ones(10)
# #6
dizi = np.linspace(0,100,5)
#7
dizi = np.random.randint(10,30,5)
#8
dizi = np.random.randn(10) 
#9
dizi = np.random.randint(10,50,15) # 3 e 5 lik olduğu için 15 elemanlı olmalı
dizi = dizi.reshape(3,5)
#10
matris = np.random.randint(10,50,15).reshape(3,5)

satirtoplam = matris.sum(axis=1)
sütuntoplam = matris.sum(axis=0)

# print(matris)
# print(satirtoplam)
# print(sütuntoplam)

#11
max = matris.max()
min = matris.min()
ort = matris.mean()
#12
maxindeks = matris.argmax()
minindeks = matris.argmin()

#13
dizi = np.arange(10,20)

sonuc = dizi[:3] # dizi[0:3] böyle de yazılır
#14
dizi = np.arange(10,20)
ters = dizi[::-1]
# print(dizi)
# print(ters)

#15
sonuc = matris[0]
#16
sonuc = matris[1,2]
print(matris)
# print(sonuc)

#17
sonuc = matris[:,0]
# print(sonuc)

#bu benden olsun
sonuc = np.sqrt(matris)
# print(sonuc)
#18
sonuc = matris **2
# print(sonuc)

#19
# sonuc = matris % 2 ==0  # True False değerleri gösterir ben direkt sayıları alsın istiyorum
matris = np.random.randint(-50,50,15).reshape(3,5)
print(matris)
ciftler = matris[ matris % 2 == 0]
sonuc = ciftler[ciftler>0]
print(sonuc)

print(dizi)