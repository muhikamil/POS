class Barang:
    def __init__(self,namabarang,harga,stock):
        self.__nama=namabarang
        self.__harga=harga
        self.__stock=stock

    #Ini Getter
    @property
    def tampil(self):
        return [self.__nama, self.__harga,self.__stock]
    
    #Ini Setter
    @tampil.setter
    def tampil(self,val):
        nBarang, hBarang, sBarang = val
        self.__nama = nBarang
        self.__harga = hBarang
        self.__stock = sBarang
