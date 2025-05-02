class ogretmen:

    def __init__(self, id, brans, ad, soyad, dogumTarihi, cinsiyet):

        if id is None:
            self.id=0
        else:
            self.id = id
        
        self.brans = brans
        self.ad = ad
        self.soyad=soyad
        self.dogumTarihi = dogumTarihi
        self.cinsiyet = cinsiyet