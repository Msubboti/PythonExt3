class Goods:
    def __init__(self, name, number=1):
        self.name = name
        self.number = number
    products = {
                    'Cheese': (107, "EDIBLE", 'KG'),
                    'Pepsi Max': (23, "EDIBLE", "piece"),
                    'Milk': (19.7, "EDIBLE", "piece"),
                    'Beef': (130, "EDIBLE", 'KG'),
                    'Soap': (15, 'CHEM', "piece"),
                    'Hand Wash': (40, 'CHEM', "piece"),
                    'Shampoo': (120, 'CHEM', "piece")
                }


    def is_eatable(self):
        Object = self.products[self.name]
        if Object[1] == "CHEM":
            pass
        else:
            return True

    def price_total(self):
        Object = self.products[self.name]
        number = self.number

        price = Object[0] * number
        return price

class Basket():

    def Total(self,list_products):
        total_price = 0
        for item in list_products:
            object = Goods(item[0], item[1])
            total_price += object.price_total()
        return total_price

    def Totally_eatable(self, list_products):

        for item in list_products:
            object = Goods(item[0], item[1])
            if object.is_eatable() == True:
                pass
            else:
                return False
        return True


if __name__=="__main__":
    print("----------Baskets----------")

    cart1 = (('Pepsi Max', 3), ('Milk', 2), ('Shampoo', 1))
    obj2 = Basket()
    print(obj2.Total(cart1))
    print(obj2.Totally_eatable(cart1))


    obj2 = Basket()
    cart2 = (('Pepsi Max', 3), ('Milk', 2), ('Cheese', 0.800), ('Beef', 2.350))
    print(obj2.Total(cart2))
    print(obj2.Totally_eatable(cart2))

    print("----------Products----------")

    obj1 = Goods("Cheese", 0.600)
    print(obj1.is_eatable())
    print(obj1.price_total())

    obj2 = Goods('Shampoo', 3)
    print(obj2.is_eatable())
    print(obj2.price_total())


