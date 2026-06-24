



#create db
import sqlite3
con=sqlite3.connect("goodcompany.db")
cur=con.cursor()
cur.execute("""create table if not exists employee(
              empid int Primary Key,
              empnam text, 
              empsal int,
              empexp float )""")
con.commit()
print("database and employee table created suceesfully")
con.close()

def insert_rec(
    
)

#write to db
import sqlite3
con=sqlite3.connect("goodcompany.db")
cur=con.cursor()
print("1.input employeee detils\n2.display employe details based one eid\n3.exit\n4.delete emp details based on eid\n5.update emp details based on emp id " )
while True:
    ch=int(input("enter choice:"))
    if ch==1:
        eid=int(input("enter emp id:"))
        enam=input("enter emp name:")
        esal=int(input("enter emp sal:"))
        eexp=float(input("enter employee experience:"))
        try:
            cur.execute("insert into employee values(?,?,?,?)",(eid,enam,esal,eexp))
            con.commit()
            print("rec inserted successfully")
        except sqlite3.IntegrityError:#not handling integrity error ie. when entered id is entered again and again
            print("trying to enter a empid that already exist")
    elif ch==2:
        sid=int(input("enter emp id to display emp details:"))
        cur.execute("select * from employee")
        rows=cur.fetchall()
        for r in rows:
            if sid==r[0]:
                print('empname:',r[1])
                print('empsal:',r[2])
                print('empexp:',r[3])
                break
        else:
            print(f"{sid} not found")
    elif ch==3:
        print("==program completed succesfully==")
        break
    elif ch==4:
        sid=int(input("enter emp id to delete emp details:"))
        cur.execute("select * from employee")
        rows=cur.fetchall()
        for r in rows:
            if sid==r[0]:
                cur.execute("delete from employee where empid= ?",(sid,))
                con.commit()
                print("record deleted successfully")
                break
        else:
            print(f"{sid} not found")
    elif ch==5:
        sid=int(input("enter emp id to update emp details:"))
        cur.execute("select * from employee")
        rows=cur.fetchall()
        for r in rows:
            if sid==r[0]:
                nnam=input("enter emp name:")
                nsal=int(input("enter updated sal:"))
                nexp=float(input("enter updated experience:"))
                cur.execute("""update employee
                            set empnam=?,empsal=?,empexp=?
                            where empid=?""",(nnam,nsal,nexp,sid))
                con.commit()
                print("record updated succesfuly")
                break
        else:
            print(f"{sid} not found.pls enter correct employee id")

            
    
    else:
        print("enter a proper choice")

con.close()
  



#read db