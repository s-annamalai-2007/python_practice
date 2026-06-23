class arith():
    def getval(self):
        self.a=int(input("enter a num:"))
        self.b=int(input("enter a num"))
class sum(arith):
    def sum(self):
        c=self.a+self.b
        print("sum=",c)
s=sum()
s.getval()
s.sum()
