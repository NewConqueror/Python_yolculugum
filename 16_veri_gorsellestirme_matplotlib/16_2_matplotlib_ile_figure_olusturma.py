import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2
# fig,axs = plt.subplot() bu şekilde yapabiliyorduk 

figure = plt.figure()  # bu şekilde de figure oluşturabiliriz grafiği görmek için figure gerekli axes i napıcaz

axes_küp = figure.add_axes([0.1,0.1,0.8,0.8]) # soldan 0.1 yani yüzde 10 alttan 0.1  genislik 0.8 yükseklik 0.8 1 üzerinden
#                                           axes i de böyle ekliyoruz
axes_küp.plot(x,y,"b")                        # color şeyi de böyleymiş 
axes_küp.set_xlabel("X ekseni")
axes_küp.set_ylabel("Y ekseni")
axes_küp.set_title("küp")

# figure üzerine bir axes daha eklenebilir şimdi z yi oluşturucaz

axes_kare = figure.add_axes([0.15,0.6,0.25,0.25]) # bir axes in içine ekledik yeni axes i

axes_kare.plot(x,z,"r")
axes_kare.set_xlabel("X ekseni")
axes_kare.set_ylabel("Y ekseni")
axes_kare.set_title("kare")


figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z, label="kare")
axes.plot(x,y, label="küp")

plt.legend(loc=2) # 1 sağ üst 2 sol üst 3 sol alt 4 sağ alt


fig,axes = plt.subplots(nrows=2,ncols=1) # fig,axes = plt.subplots(2,1) 2 satır 1 sütun demek zaten ama biz söyledik

# fig,(axes1,axes2) = plt.subplots(nrows=2,ncols=1) # böyle yazsaydık böyle ulaşıcaktık
# axes1 =
# axes2 = vs

axes[0].plot(x,z)
axes[0].set_title("kare")
axes[1].plot(x,y)
axes[1].set_title("küp")

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8)) # figsize ile figure ün boyutunu ayarlayabiliriz

plt.tight_layout()

fig.savefig("figure1.png") # png olarak kayıt eder
fig.savefig("figure1.pdf") # pdf olarak kayıt eder

plt.show()