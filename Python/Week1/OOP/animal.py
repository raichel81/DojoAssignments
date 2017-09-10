class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 0
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.name, "has health of:"
        print self.health
        return self
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)   # use super to call the Animal __init__ method
        self.health = 150             # every Dog starts off with 150 health        
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)    
        self.health = 170 
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print 'I am a Dragon'

'''Create an instance of the Animal, have it walk() three times, 
run() twice, and finally displayHealth() to confirm that 
the health attribute has changed.

Have the Dog walk() three times, run() twice, pet() once, 
and have it displayHealth().

Now try creating a new Animal and confirm that it can 
not call the pet() and fly() methods, and its displayHealth() 
is not saying 'this is a dragon!'. Also confirm that your Dog 
class can not fly().'''

a = Animal("George")
a.walk().walk().walk().run().run().display_health()
d = Dog("Benedict")
d.walk().walk().walk().run().run().pet().display_health()
dragon = Dragon("Bob")
dragon.display_health()
dragon.pet().display_health()