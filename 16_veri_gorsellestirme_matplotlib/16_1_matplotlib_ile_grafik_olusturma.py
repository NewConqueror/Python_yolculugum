import matplotlib.pyplot as plt
import  numpy as np

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x)  # sadece bir tane verirsen o y eksenine yerleşir x eksenine default kendi değer atar
plt.plot(x,y) # ilk verdiğin x eksenine ikinci verdiğin y eksenine yerleşir

plt.axis([0,6,0,20]) # x in min değeri max değeri  y nin min değeri max değeri

plt.title("Grafik Başlığı")     # title  ile Grafiğe başlık yazmak için kullanırız
plt.xlabel("X ekseni")          # xlabel ile X eksenine isim veririz
plt.ylabel("Y ekseni")          # ylabel ile Y eksenine isim veririz

plt.plot(x,y, color ="red", linewidth="5") # rengi kırmızı kalınlığı ise 5 yaptık

plt.plot(x,y, "-g")  # yeşil normal çizgi gelir
plt.plot(x,y, "--g") # yeşil kesikli çizgi gelir

plt.plot(x,y, "o--b") # marker ekledik değeri işaretleyen şey yani "o" yuvarlak demek çizgi kesikli rengi mavi


x = np.linspace(0,2,100)

plt.plot(x, x,    label="lineer",    color="blue")      # lineer quadratik kübik diye isim verdik
plt.plot(x, x**2, label="qudratik", color="yellow")
plt.plot(x, x**3, label="kübik",    color="red")

plt.xlabel("X ekseni")
plt.ylabel("Y ekseni")

plt.legend() # grafikte herhangi bir yere bilgilendirme yapar işte mavi olan lineer sarı olan quadratik vs vs gibi


x = np.linspace(0,2,100)

fig,axs = plt.subplots(3) # alt alta 3 tane axes alanı oluşturur 

axs[0].plot(x, x, color="red")
axs[0].set_title("lineer")             # her birinin grafiğine bir başlık verdik ama iç içe girdiler

axs[1].plot(x, x**2, color="green")
axs[1].set_title("quadratik")         

axs[2].plot(x, x**3, color="blue")
axs[2].set_title("kübik")

plt.tight_layout()                   # bu başlıkların birbiri içine girmesini düzeltti



x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2) # 2 ye 2 lik bir axes alanı oluşturur 

fig.suptitle("Grafik Başlığı") # axes alanının ana başlığı olucak

axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="blue")
axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="yellow")


import pandas as pd

df = pd.read_csv("nba.csv")

df = df.drop(["Number"], axis=1).groupby("Team").mean() #Number sütununu sildik ve Takıma göre gruplayıp ortalama aldık

df.head().plot(subplots=True)  #subplots True dediğimiz için kendisi her sütun için ayrı bir grafik oluşturucak 
#                               Age Salary Weight vs yani alt alta 3 tane grafiğimiz olucak 

plt.legend()

plt.show()                      # grafiği görmek için bunu çalıştırmamız gerekiyor adı üstünde show göster
