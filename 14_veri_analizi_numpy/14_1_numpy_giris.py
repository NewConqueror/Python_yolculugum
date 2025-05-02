# veri analizinde yaygın olarak kullanılan bir kütüphanedir  

# numpy kullanmamızın nedeni normal listelerin yapamadığı bir çok işlemi numpy kütüphanesi üzerinden yapabiliyoruz

# büyük bir veri geldiğinde o verileri numpy objeleri içerisine alıp kullanmamız daha mantıklı

# çünkü numpy nesneleri normal listelere göre daha az yer kaplar çok daha hızlı çalışır ve metotları daha çok

import numpy as np

# python list
py_liste = [1,2,3,4,5,6,7,8,9]

# numpy array

np_dizi = np.array([1,2,3,4,5,6,7,8,9]) # parametre olarak bir liste vermeliyiz

print(type(py_liste))  # list tipinde
print(type(np_dizi))  # numpy.ndarray tipinde


# çok boyutlu bir dizi oluşturmak istersek

py_multi = [[1,2,3],[4,5,6],[7,8,9]]

np_multi = np_dizi.reshape(3,3) # 3 e 3 lük bir matrise çevir demiş olduk

print(py_multi) # [[1,2,3],[4,5,6],[7,8,9]] şeklinde yazdırır
print(np_multi) # matris şeklinde yazdırmış olur 

print(np_dizi.ndim) # bize kaç boyutlu olduğunu söyler dimensional dan geliyor 1
print(np_multi.ndim) # 2 yazar

print(np_dizi.shape) # kaça kaçlık olduğunu bize söyler (9,) yani 9 a 1 lik yani 9 elemanlı 1 boyutlu
print(np_multi.shape)# (3,3) yazar yani 3 e 3 lük bir matris olduğunu bize söyler