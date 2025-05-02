class sinif:

    def __init__(self, id, ad, ogretmenid):

        if id is None:
            self.id=0
        else:
            self.id = id
            
        self.ad = ad
        self.ogretmenid = ogretmenid

    @staticmethod
    def sinifOlustur(nesne):
        
        liste = []

        for i in nesne:
            liste.append(sinif(i[0],i[1],i[2]))

        return liste

       