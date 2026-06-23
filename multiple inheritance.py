#a+b=c
class sum:
    def getsum(self):
        self.a=int(input("enter a num:"))
        self.b=int(input("enter a num:"))
class product:
    def getmul(self):
        self.x=int(input("enter a num:"))
        self.y=int(input("enter a num:"))
class arithmetic(sum,product):
    def add(self):
        c=self.a+self.b
        print("sum=",c)
    def mul(self):
        c=self.x*self.y
        print("product=",c)
a=arithmetic()
print("= enter input for adding=")
a.getsum()
a.add()
print("= enter input for multiplying=")
a.getmul()
a.mul()




