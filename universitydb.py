import sqlite3

con=sqlite3.connect("student_life.db")
cur=con.cursor()
cur.execute("""create table if not exists transcript(
            c_code text primary key,
            c_title text,
            c_credit integer,
            grade text)
""")
print("db and table created successfully")
con.commit()
con.close()

con=sqlite3.connect("student_life.db")
cur=con.cursor()
print("1.insert rec\n2.update rec\n3.delete rec\n4.display record\n5.close")
#inserting record
while True:
    ch=int(input("enter your choice:"))
    if ch==1:#insert
        c_code=input("enter code of subject:")
        c_title=input("enter title of subject:")
        c_credit=int(input("enter credit of subject:"))
        grade=input("enter grade of subject:")
        try:
            cur.execute("insert into transcript values(?,?,?,?)",(c_code,c_title,c_credit,grade))
            con.commit()
            print("record inserted successfully")
        except sqlite3.IntegrityError:
            print("exist already")
    elif ch==2:
        s_code=input("enter subject code to change grade:")
        u_grade=input("enter new grade of subject:")
        cur.execute("""update transcript 
                    set grade=?
                    where c_code=? """,(u_grade,s_code))
        con.commit()
        if cur.rowcount==1:#or cur.rowcount>0:
            print("record updated successfully")
        else:
            print(f"{s_code} does not exist")
    elif ch==3:
        s_code=input("enter subject code to delete record:")
        cur.execute("delete from transcript where c_code=?",(s_code,))
        con.commit()
        if cur.rowcount==1:#or cur.rowcount>0:
            print("record deleted successfully")
        else:
            print(f"{s_code} does not exist")
    elif ch==4:#no records to display is displayed along with records even if the records are present
        cur.execute("select * from transcript")
        rows=cur.fetchall()
        if len(rows)>0:
            for r in rows:
                print(f"[{r[0]}]:[{r[1]}]-current grade:[{r[3]}]")

        else:
            print("no records to display")
    elif ch==5:
        con.close()
        print("==program completed successfully==")
        break




'''
try:
    cur.execute("insert into transcript values(c_code,c_title,c_credit,grade)")
    con.commit()
    print("record inserted successfully")

except IntegrityError:
    print("enter correct detail")
    '''