class lion:
    def sound(self):
        print("roar roar")
class dog(lion):
    def sound(self):
        print("bow bow")
class cat(dog):
    def sound(self):
        print("meo meow")
c=cat()#only called class functiom is executed although every thing as same function
c.sound()