n=int(input('enter a num:'))
tem=n
n=abs(n)
s=0
while(n!=0):
    dig=n%10
    s=s+dig
    n=n//10
print('sum=',s)

'''

n=-4
print(n//10)
'''