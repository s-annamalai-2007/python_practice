'''class greetings():
    def greet(self,name):
        print(f"welcome {name}") 
g=greetings()
g.greet("anand")
'''

'''class greetings():
    def __init__(self):
        self.name=input("enter your name:")
    def display(self):
        print("welcome:",self.name)
s1=greetings()
s1.display()
s2=greetings()
s2.display()
'''

'''class greetings():
    def __init__(self):
        self.name=input("enter your name:")
        print("welcome:",self.name)
s1=greetings()
s2=greetings()
'''

'''#4
class greetings():
    def __init__(self):
        self.name=input("enter your name:")
    def display(self):
        print("welcome:",self.name)
    def update(self):
        self.name=input("enter your updated name:")
print("student 1:")
s1=greetings()
s1.display()


s1.update()
s1.display()

print("student 2:")
s2=greetings()
s2.display()
print("==program completed succesfully==")
'''


#or 4
class greetings():
    def __init__(self):
        self.name=input("enter your name:")
    def display(self):
        print("welcome:",self.name)
    def update(self):
        self.name=input("enter your updated name:")


print("enter inputs of all students:")
s1=greetings()
s2=greetings()

print("1.display\n2.update\n3.exit program")

while True:
    ch=int(input("enter your choice:"))
    if ch==1:
        print("entered stu information are:")
        s1.display()
        s2.display()
    elif ch==2:
        print("change the input of students:")
        s1.update()
        s2.update()
    elif ch==3:
        print("==program completed succesfully==")
        break
    else:
        print(" enter a proper choice")


        
        





