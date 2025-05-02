# beatiful soup un yaptığı işlem html bilgisini istediğimiz şekilde filtreleme title ı getir h1 i getir vs gibi

html_dokümani = """
iskelet oluşturmak lazim
head ve body var  ve hepsinde birer etiket var açılış etiketi kapanış etiketi vs
head internete tanıtım bütün tasarım aslında body kısmında
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>

<body>
    <h1 id="header">
        h1 Başlık eklemek için kullanılır 
    </h1>
 
    ileride bir şey değiştireceksem header ile çağırmam yeterli yani id si header olana git diyoruz

    <div class="grup1">
        
        <h2>
            h2 ile altbaşlık ekleriz başlık 1 tane ama altbaşlık birkaç tane olabilir
        </h2>

        <ul>
        liste eklemek için ul deriz 

        <li>
            ve her bir liste elemanı li ile ifade edilir
        </li>

        <li>
            menü
        </li>

        <li>
            lö menü 
        </li>

        </ul>

    </div>

    div lerden sadece class ı grup1 olan veya sadece grup2 olanı çağırabilirim

<div class="grup2">
        
        <h2>
            birden fazla da div ile grup yapabiliriz
        </h2>

        <ul>
        liste eklemek için ul deriz 

        <li>
            ve her bir liste elemanı li ile ifade edilir
        </li>

        <li>
            menü
        </li>

        <li>
            lö menü 
        </li>

        </ul>

    </div>

    <div class="grup3">
        
        <h2>
            birden fazla da div ile grup yapabiliriz
        </h2>

        <ul>
        liste eklemek için ul deriz 

        <li>
            ve her bir liste elemanı li ile ifade edilir
        </li>

        <li>
            menü
        </li>

        <li>
            lö menü 
        </li>

        </ul>

    </div>


    <img src="C:\Users\Halime\OneDrive\Masaüstü\FATİH\doctor qho.jpg" alt=""> yol vermezsen kendi dizinine bakar verirsen oraya gider
    
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>

"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_dokümani, "html.parser")

sonuc = soup.prettify() # karışık dokümanı düzeltilmiş olarak bize getirir 

sonuc = soup.title # bütün title etiketleriyle vs beraber gelir
sonuc = soup.head  # bütün head etiketleri gelir
sonuc = soup.body  # bütün body etiketleri gelir

sonuc = soup.title.name # etiketin ismi gelir title yani
sonuc = soup.title.string # etiketin içi gelir yani ilk web sayfam yazısı

sonuc = soup.h1         # yine etiket olduğu gibi gelir
sonuc = soup.h1.string  # etiketin içi gelir yani h1 Başlık eklemek için kullanılır 

sonuc = soup.h2         # etiket olduğu gibi gelir ama ilk h2 2. h2 yi göstermez sadece ilki
sonuc = soup.h2.name    # etiket ismi gelir  yani sadece h2
sonuc = soup.h2.string  # ilk h2 nin içeriği gelir h2 ile altbaşlık ekleriz başlık 1 tane ama altbaşlık birkaç tane olabilir

sonuc = soup.find_all("h2")     # yukarıdaki eksiği kapatır bütün h2 leri bize gösterir
sonuc = soup.find_all("h2")[0]  # 1. h2
sonuc = soup.find_all("h2")[1]  # 2. h2 yi bize getirir

sonuc = soup.div              # sadece ilk div i bize getirir
sonuc = soup.find_all("div")  # bütün div leri getirir yani grup1 ve grup2 yi
sonuc = soup.find_all("div")[1] # 2. div i yani grup 2 yi alırız
sonuc = soup.find_all("div")[1].ul # 2.div in altındaki ul yi bize gösterir
sonuc = soup.find_all("div")[1].ul.li # dersek sadece 1.li yi getirir
sonuc = soup.find_all("div")[1].ul.find_all("li") # 2. divin altındaki ul nin altındaki bütün li leri getirir


sonuc = soup.div.findChildren() # div in altındaki bütün her şeyi yani çocukları gösterir 

sonuc = soup.div.findNextSibling().findNextSibling() # grup 3 ü gösterir 1 in next i 2 2 nin nexti 3

sonuc = soup.div.findNextSibling().findNextSibling().findPreviousSibling() # dersek grup 2 ye geri dönmüş oluruz


sonuc = soup.find_all("a") # bütün a yı getirir

for link in sonuc:
    print(link)   # bütün a yı düzgün bir şekilde yazar


for link in sonuc:
    print(link.get("href")) # bu şekilde yaparak içinden istediğimiz özelliği çekebiliriz

print(sonuc)