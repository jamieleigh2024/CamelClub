class Camel:
    """
    This class represents Camel Club, Huddersfield, UK
    """

    def __init__(self, staff_name):
        self.guests = 0
        self.money_gbp = 10000
        self.entrance_fee = 6
        self.vk_bottle = VK()
        self.champagne_bottle = Champagne()
        self.staff = Staff(name=staff_name)

    def sell_drink(self, drink_type):
        if isinstance(drink_type, VK):
            self.vk_bottle.sell_vk()
            self.staff.takings += self.vk_bottle.price
        if isinstance(drink_type, Champagne):
            self.champagne_bottle.sell_champagne()
            self.staff.takings += self.champagne_bottle.price

    def guest_arrives(self, age):
        if age < 18:
            return print("Guest not permitted due to age")
        elif age >= 18:
            self.money_gbp += self.entrance_fee
            self.guests += 1

    def guest_leaves(self):
        self.guests -= 1


class VK:

    def __init__(self):
        self.type = "VK"
        self.cost = 1
        self.price = 4
        self.vk_bottles = 1200
        self.min_vk_bottles = 1200

    def order_vk(self):
        vk_amount = self.min_vk_bottles - self.vk_bottles
        self.vk_bottles += vk_amount

    def sell_vk(self):
        self.vk_bottles -= 1


class Champagne:

    def __init__(self):
        self.type = "Champagne"
        self.cost = 25
        self.price = 60
        self.champagne_bottles = 1200
        self.min_champagne_bottles = 1200

    def order_champagne(self):
        champagne_amount = self.min_champagne_bottles - self.champagne_bottles
        self.champagne_bottles += champagne_amount

    def sell_champagne(self):
        self.champagne_bottles -= 1


class Staff:

    def __init__(self, name):
        self.name = name
        self.takings = 0
