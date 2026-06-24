d={}
print("1.input employeee detils\n2.display employe details based one eid\n3.exit" )
while True:
    ch=int(input("enter choice:"))
    if ch==1:
        eid=int(input("enter emp id:"))
        enam=input("enter emp name:")
        esal=int(input("enter emp sal:"))
        eexp=float(input("enter employee experience:"))
        #d={eid:[enam,esal,eexp]}
        d[eid]=[enam,esal,eexp]
    elif ch==2:
        sid=int(input("enter emp id to display emp details:"))
        for k in d:
            if k==sid:
                print("ename:",d[k][0])
                print("esal:",d[k][1])
                print("eexp:",d[k][2])
                break
        else:
            print("entered eid not found")#else:
                #print("entered eid not found")
    elif ch==3:
        print("==program completed succesfully==")
        break
    else:
        print("pls enter a proper choice")