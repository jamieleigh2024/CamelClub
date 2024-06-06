class Camel:
    """
    This class represents Camel Club, Huddersfield, UK
    """

    def __init__(self):
        self.guests = 0
        self.money_gbp = 10000
        self.entrance_fee = 6
        self.vk_bottles = VK()
        self.champagne_bottles = Champagne()

    def sell_drink(self, drink_type):
        if isinstance(drink_type, VK):
            self.vk_bottles.sell_vk()
        if isinstance(drink_type, Champagne):
            self.champagne_bottles.sell_champagne()

    def guest_arrives(self):
        self.money_gbp += self.entrance_fee
        self.guests += 1

    def guest_leaves(self):
        self.guests -= 1


class Bottle:
    def __init__(self):
        self.vk_bottles = 1200
        self.champagne_bottles = 1200
        self.min_vk_bottles = 1200
        self.min_champagne_bottles = 1200


class VK(Bottle):

    def __init__(self):
        super().__init__()
        self.type = "VK"
        self.cost = 1
        self.price = 4

    def order_vk(self):
        vk_amount = self.min_vk_bottles - self.vk_bottles
        self.vk_bottles += vk_amount

    def sell_vk(self):
        self.vk_bottles -= 1


class Champagne(Bottle):

    def __init__(self):
        super().__init__()
        self.type = "Champagne"
        self.cost = 25
        self.price = 60

    def order_champagne(self):
        champagne_amount = self.min_champagne_bottles - self.champagne_bottles
        self.champagne_bottles += champagne_amount

    def sell_champagne(self):
        self.champagne_bottles -= 1