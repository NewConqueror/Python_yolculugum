list = [1,2,3]
tuple =[1,"iki",3.5]

print(list)
print(tuple) # ikisi de ayrı birer tip diye geçer tıpkı float int vs gibi

print(list[2])
print(tuple[2]) # normal listede olduğu gibi tuple da da böyle yazdırabiliyoruz indexteki elemanı

print(len(list))
print(len(tuple)) # aynı şekilde çalışır ve eleman sayısını verir

list = ["ali","veli"]
tuple = ["damla","ayşe","ayşe"] # 0 dan yeni bir atama yapabiliyoruz

list[0] = "ahmet" # normal listede spesifik bir index değiştirmeye izin veriyor
# tuple[0] = "cemre" # ama tuple da spesifik bir index değiştiremiyoruz hata veriyor
# bütün tuple u yukarıdaki gibi değiştirebiliriz ama özel bir index i değiştiremeyiz

print(tuple.count("ayşe")) # count fonksiyonu aynı şekilde çalışır
print(tuple.index("ayşe")) # index fonksiyonu aynı şekilde çalışır

names = ["cemre","saliha","emel"] + tuple # normal peşi sıra ekler cemre saliha emel damla ayşe ayşe olur yenisi
print(names)


