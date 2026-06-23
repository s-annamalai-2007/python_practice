class arith():
    def getval(self):
        self.a=int(input("enter a num:"))
        self.b=int(input("enter a num"))
class sum(arith):
    def sum(self):
        c=self.a+self.b
        print("sum=",c)
class product(sum):
    def mul(self):
        c=self.a*self.b
        print("product=",c)

p=product()
p.getval()
p.sum()
p.mul()