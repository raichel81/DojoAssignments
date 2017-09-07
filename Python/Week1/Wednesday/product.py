
'''Assignment: Product
The owner of a store wants a program to track products. Create a product class 
to fill the following requirements.

Product Class:
Attributes:

• Price

• Item Name

• Weight

• Brand

• Cost

• Status: default "for sale"

Methods:

• Sell: changes status to "sold"

• Add tax: takes tax as a decimal amount as a parameter and returns the price of the 
item including sales tax

• Return: takes reason for return as a parameter and changes status accordingly. 
If the item is being returned because it is defective change status to defective 
and change price to 0. If it is being returned in the box, like new mark it as for sale. 
If the box has been opened set status to used and apply a 20% discount.

• Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be 
chained.'''

class Product(object):
    def __init__(self, price, name, weight, brand,cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self,tax):
        self.price = self.price + (self.price*tax)
        return self
    def returned(self,reason):
        self.status = reason
        if reason == "defective":
            self.price = 0
            return self
        elif reason == "like new":
            self.status == "for sale"
            return self
        elif reason == "opened":
            self.status = "used"
            self.price = self.price *.8
            return self
    def display_info(self):
        print "Price: ", self.price
        print "Name: ", self.name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Cost: ", self.cost
        print "Status: ", self.status
        return self

product1 = Product(25, "doll", "3lb", "gerber", 30)
product1.sell().add_tax(.03).returned("opened").display_info()