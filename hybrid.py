#a+b->c->d
class sum:
    def getsum(self):
        self.a=int(input("enter a num to add :"))
        self.b=int(input("enter a num to add:"))
class product:
    def getmul(self):
        self.x=int(input("enter a num to mul:"))
        self.y=int(input("enter a num to mul:"))
class arithmetic(sum,product):
    def cal(self):
        self.c=self.a+self.b
        self.z=self.x*self.y
class disp(arithmetic):
    def display(self):
        print(self.c,"is sum")
        print(self.z,"is product")

d=disp()
d.getsum()
d.getmul()
d.cal()
d.display()