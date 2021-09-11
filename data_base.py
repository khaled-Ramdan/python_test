import sqlite3
import sys
from random import random
import math
db=sqlite3.connect(r"D:\programs and design\visual stadio\python\app.db")
db.execute("CREATE TABLE IF NOT EXISTS USERS (user_id INTEGER, name TEXT,progress INTEGER)")
user_id = math.floor(random()*10000)
cr=db.cursor()
def com_close():
    db.commit()
    db.close()
def add():
    name = input("ENter Name: ")
    pro = input("Enter your progress: ")
    cr.execute(f"insert into users(user_id,name,progress) values({user_id}, '{name}','{pro}')")
    com_close()
def update():
    id =int(input("Enter id: "))
    name = input("ENter new Name: ")
    pro = input("Enter your new progress: ")
    cr.execute(f"update users set name = '{name}' where user_id = {id}")
    cr.execute(f"update users set progress = '{pro}' where user_id = {id}")
    com_close()
def delete():
    id =int(input("Enter id: "))
    cr.execute(f"delete from users where user_id = {id}")
    com_close()
def show():
    ch = input("1-all => show all database\n2-one => show with a specific id\nchoice: ").strip().lower()
    while ch != "all" and ch !="one":
        ch = input("wrong choice.\n1-all => show all database\n2-one => show with a specific id\nchoice: ")
    if(ch=="all"):
        x= input("1- ordered by name =>name\n2-ordered by id=>id\nchoice: ").strip().lower()
        while x!="name"  and  x!="id":
            x= input("wrong choice\n1- ordered by name =>name\n2-ordered by id=>id\nchoice: ").strip().lower() 
        if x=="id": x="user_id"
        cr.execute(f"select * from users order by {x}")
    else:
        id = int(input("Enter user id : "))
        cr.execute(f"select * from users where user_id = {id}")
    my_list = cr.fetchall()
    if(not len(my_list)):
        print("there are no any skills")
    else:
        print(f"showing skills\nthere are {len(my_list)}: ")
        for i,j in enumerate(my_list):
            print(f"{i+1}- skill name:  {j[1]} progress: {j[2]} id: {j[0]}")
    com_close()





my_input="""
    1- add a member
    2- update a member
    3- delete a member
    4- show skill member
    YOUR CHOICE: \
"""
user_input=input(my_input)
while user_input !="1" and user_input !="2"and user_input !="3"and user_input !="4" :
    user_input=input(my_input)

if user_input=="1":
    add()
elif user_input=="2":
    update()
elif user_input=="3":
    delete()
else : 
    show()
