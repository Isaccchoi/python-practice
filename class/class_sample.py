class Shop(object):
    def __init__(self, name, shop_type, address):
        self.name = name
        self.address = address
        self._shop_type = shop_type

    def show_info(self):
        print("상점정보 (<%s>)"%(self.name))
        print(f"\t유형: {self._shop_type}")
        print(f"\t주소: {self.address}")

    @staticmethod
    def make_dummy():
        return Shop("untitled", "undefined", "unknown")


    def change_type(self, new_shop_type):
        self._shop_type = new_shop_type

    @property
    def shop_type(self):
        return self.shop_type

    @shop_type.setter
    def name(self, new_shop_type):
        self._shop_type = new_shop_type


class Restaurent(Shop):
    def __init__(self, name, shop_type, address, rating):
        super().__init__(self, name, shop_type, address)
        self.raging = rating
        
    def show_info(self):
        print("식당 정보 (<%s>)"%(self.name))
        print(f"\t유형: {self._shop_type}")
        print(f"\t주소: {self.address}")
