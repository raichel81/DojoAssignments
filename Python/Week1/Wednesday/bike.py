'''Assignment: Bike
Create a new class called Bike with the following properties/attributes:

price
max_speed
miles
Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance 
(e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the 
initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5.
..
Have the first instance ride three times, reverse once and have it displayInfo(). 
Have the second instance ride twice, reverse twice and have it displayInfo(). 
Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods?'''

class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        print "Riding"
        self.miles += 10
        print self.miles
        return self
    def reverse(self):
        if self.miles >= 5:
            print "Reversing"
            self.miles -= 5
            return self
        else:
            print "Trying going somewhere first!"
            return self
    def display_info(self):
        print self.price
        print self.max_speed
        print self.miles

bike1 = Bike(200,"25mph")
bike1.ride().ride().ride().reverse().display_info()
bike2 = Bike(350, "30mph")
bike2.ride().ride().reverse().reverse().display_info()
bike3 = Bike(100, "20 mph")
bike3.reverse().reverse().reverse().display_info()

