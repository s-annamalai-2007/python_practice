#q_str = "Q -"
#q_count = 0
'''
with open('qa.txt',"w") as fp:
    fp.write("""Welcome to the Q1 Earnings Call. First, the CEO will give some opening remarks. 
We had a great quarter and revenue is up by 10%. Now we will open the floor to Q&A.

Q - John Doe (Goldman Sachs): Can you explain why margins 
improved this quarter?
A - Tim Cook (CEO): Thanks John. We optimized our supply 
chain and reduced freight costs.

Some random operator transition text goes here.

Q - Jane Smith (Morgan Stanley): What are your growth expectations
 for next quarter?
A - Luca Maestri (CFO): We are targeting a 5% sequential growth
 in the next quarter.""")
    print('file created successfully')
    '''

q_str='Q -'
q_count=0
a_str='A -'
a_count=0

flag=-1

fp1=open("q.txt",'w')
fp2=open("a.txt",'w')
fp3=open("others.txt",'w')

with open('qa.txt','r') as fp:
    ll=fp.readlines()
    for l in ll:
        if l.find(q_str)==0:
            q_count+=1
            fp1.write(l)
            flag=1

        elif l.find(a_str)==0:
            a_count+=1
            fp2.write(l)
            flag=0
        else:
            if flag==1:
                fp1.write(l)
            elif flag==0:
                fp2.write(l)
            else:
                fp3.write(l)
    print(q_count)
    print(a_count)

                
                    

