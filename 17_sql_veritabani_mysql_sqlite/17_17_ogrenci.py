class ogrenci:

    def __init__(self, id, numara, ad, soyad, dogumTarihi, cinsiyet, sinifid):

        if id is None:
            self.id=0
        else:
            self.id = id
        
        self.numara = numara
        self.ad = ad
        self.soyad=soyad
        self.dogumTarihi = dogumTarihi
        self.cinsiyet = cinsiyet
        self.sinifid = sinifid

    @staticmethod
    def ogrenciOlustur(nesne):

        liste = []

        if isinstance(nesne, tuple):
            liste.append(ogrenci(nesne[0],nesne[1],nesne[2],nesne[3],nesne[4],nesne[5],nesne[6]))
        else:
            for i in nesne: 
# olm tuple sa eyvallah listeye ekliyoruz ama zaten listeyse bir şey yapmıyoruz aq yazdırıyoruz listeye ekleyince
# olay çözüldü amk artık rahat ölebilirim
             liste.append(ogrenci(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

        return liste