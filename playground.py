class Car:
    def __init__(self,**kk):
        self.ad = kk["ad"]
        self.yas = kk["yas"]

menimki = Car(ad="Rufo", yas=33)
print(menimki.ad, menimki.yas)
