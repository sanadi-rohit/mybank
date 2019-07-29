import sqlite3
import tkinter as tk

conn = sqlite3.connect('MyBank.db')
cur = conn.cursor()
choice=int(input("first time?"))
if choice:
    cur.execute("drop table if exists mybank")
    cur.execute("create table mybank(acc_no int, name char, balance int)")
    while(1):
        name=input("enter name")
        if name:
            acno=int(input("enter account number"))
            cur.execute(f"""insert into mybank values({acno},"{name}",500)""""")
        else:
            break

choice=int(input("want to see the database"))
if choice:
    cur.execute("select * from mybank")
    result = cur.fetchall()
    print(result)

root = tk.Tk()
root.title("MyBank")
root.geometry('600x400')
root.resizable(True,True)

frm1 = tk.Frame(root)
frm1.pack(fill="x")
frm2 = tk.Frame(root)
frm2.pack(fill="x", expand="true")

def donew():
    global r,accno_ent,amount_ent
    cur.execute(f"update mybank set balance=balance-{amount_ent.get()} where acc_no={accno_ent.get()}")
    r=cur.execute("select * from mybank")
    print(r)
    home()

def doned():
    global r,accno_ent,dpamount_ent
    cur.execute(f"update mybank set balance=balance+{dpamount_ent.get()} where acc_no={accno_ent.get()}")
    r=cur.execute("select * from mybank")
    print(r)
    home()

def deposit():
    global frm1,frm2,dpamount_ent
    frm1.destroy()
    frm2.destroy()
    frm1 = tk.Frame(root)
    frm1.pack(fill="x")
    dpamount_lbl = tk.Label(frm1, text="Enter amount:")
    dpamount_lbl.grid(row="0", column="0")
    dpamount_ent=tk.Entry(frm1)
    dpamount_ent.grid(row="0",column="1")
    submit2=tk.Button(frm1,text="submit",command=doned)
    submit2.grid(row=2,column=1)
def withdraw():
    global frm1,frm2,amount_ent
    frm1.destroy()
    frm2.destroy()
    frm1 = tk.Frame(root)
    frm1.pack(fill="x")
    amount_lbl = tk.Label(frm1, text="Enter amount:")
    amount_lbl.grid(row="0", column="0")
    amount_ent=tk.Entry(frm1)
    amount_ent.grid(row="0",column="1")
    submit2=tk.Button(frm1,text="submit",command=donew)
    submit2.grid(row=2,column=1)

def login():
    global frm1, frm2,accno_ent,r
    cur.execute(f"select acc_no,name,balance from mybank where acc_no={accno_ent.get()}")
    r=cur.fetchall()
    print(r)
    if r:
        frm1.destroy()
        frm2.destroy()
        frm1 = tk.Frame(root)
        frm1.pack(fill="x")
        hello = tk.Label(frm1, text=f"hi, {r[0][1]}", font="Courier")
        hello.pack(fill="x")
        whatdo = tk.Label(frm1, text="what do you want to do?", font="Courier")
        whatdo.pack(fill="x")
        withdrawbt = tk.Button(frm1, text="Withdraw", font=("times new roman", 34), command=withdraw)
        withdrawbt.pack(side="left", expand=True)
        depositbt = tk.Button(frm1, text="deposit", font=("times new roman", 34), command=deposit)
        depositbt.pack(side="right", expand=True)
    else:
        costumer()

def insert():
    global mgaccno_ent,mgname_ent
    cur.execute(f"insert into mybank values({mgaccno_ent.get()},'{mgname_ent.get()}',500)")
    home()

def manager():
    global frm1,frm2,mgaccno_ent,mgname_ent
    frm1.destroy()
    frm2.destroy()
    frm1 = tk.Frame(root)
    frm1.pack(fill="x")
    mgdetails = tk.Label(frm1, text="Enter account details", font="Courier")
    mgdetails.pack(fill="x")
    frm2 = tk.Frame(root)
    frm2.pack(fill="x")
    mgaccno_lbl = tk.Label(frm2, text="Account number:")
    mgaccno_lbl.grid(row="0", column="0")
    mgaccno_ent = tk.Entry(frm2)
    mgaccno_ent.grid(row="0", column="1")
    mgname_lbl = tk.Label(frm2, text="name:")
    mgname_lbl.grid(row="1", column="0")
    mgname_ent = tk.Entry(frm2)
    mgname_ent.grid(row="1", column="1")
    mgsubmit1 = tk.Button(frm2, text="submit", command=insert)
    mgsubmit1.grid(row=2, column=1)


def costumer():
    global frm1,frm2,accno_ent
    frm1.destroy()
    frm2.destroy()
    frm1 = tk.Frame(root)
    frm1.pack(fill="x")
    details=tk.Label(frm1,text="Enter account details",font="Courier")
    details.pack(fill="x")
    frm2 = tk.Frame(root)
    frm2.pack(fill="x")
    accno_lbl=tk.Label(frm2,text="Account number:")
    accno_lbl.grid(row="0",column="0")
    accno_ent=tk.Entry(frm2)
    accno_ent.grid(row="0",column="1")
    submit1=tk.Button(frm2,text="submit",command=login)
    submit1.grid(row=2,column=1)

def home():
    global frm1,frm2
    frm1.destroy()
    frm2.destroy()
    frm1=tk.Frame(root)
    frm1.pack(fill="x")
    frm2=tk.Frame(root)
    frm2.pack(fill="x", expand="true")
    heading=tk.Label(frm1,text="MyBank",font=("Courier", 44))
    heading.pack(fill="x")
    question=tk.Label(frm2,text="who are you?",font=("times new roman", 44))
    question.pack(fill="x")
    managerbt=tk.Button(frm2,text="Manager",font=("times new roman", 34),command=manager)
    managerbt.pack(side="left",expand=True)
    costumerbt=tk.Button(frm2,text="Costumer",font=("times new roman", 34),command=costumer)
    costumerbt.pack(side="right",expand=True)

home()
root.mainloop()
