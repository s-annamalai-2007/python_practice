'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

fp=open("anna.txt","w")
fp.write("""today is a good day. 
i saw the birds where chirriping in the rainy climate along with sun shine.
 there  were many childrens who where playing cricket in the rain.
""")
fp.close()

fp=open("anna.txt","r")
c=0
sw=input("enter a word from the paragrap to count:")
r=fp.readlines()
for l in r:
    lw=l.split()
    for w in lw:
        if w.strip(',.').lower()==sw.lower():
            c=c+1
print("count=",c)
            