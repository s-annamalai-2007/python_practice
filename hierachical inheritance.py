class arith():
    def getval(self):
        self.a=int(input("enter a num:"))
        self.b=int(input("enter a num:"))
class sum(arith):
    def sum(self):
        c=self.a+self.b
        print("sum=",c)
class product(arith):
    def mul(self):
        pd=self.a*self.b
        print("product=",pd)
s=sum()
s.getval()
s.sum()

p=product()
p.getval()
p.mul()

