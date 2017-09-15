class Shop(object):
    def __init__(self, name, shop_type, address):
        self.name = name
        self.address = address
        self.__shop_type = shop_type

    def show_info(self):
        print("상점정보 (<%s>)"%(self.name))
        print(f"\t유형: {self.__shop_type}")
        print(f"\t주소: {self.address}")

    def change_type(self, new_shop_type):
        if new_shop_type not in ['패스트푸드', 'PC방']:
            print('해당 상점 유형은 사용할 수 없습니다.')
        else:
            self.__shop_type = new_shop_type

    @property
    def shop_type(self):
        return self.shop_type

    @shop_type.setter
    def name(self, new_name):
        if new_shop_type not in ['패스트푸드', 'PC방']:
            print('해당 상점 유형은 사용할 수 없습니다.')
        else:
            self.__shop_type = new_shop_type
