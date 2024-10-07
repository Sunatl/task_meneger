import psycopg2

from  conection import conn  


cur = conn.cursor()

cur.execute("""CREATE TABLE if not exists Student (
            id SERIAL PRIMARY KEY,
            name VARCHAR (50) UNIQUE NOT NULL,
            age int,
            email VARCHAR (20) NOT NULL)
            """)
conn.commit()
cur.close()



def add():
    cur = conn.cursor()
    name = input("name: ")
    age = int(input("age: "))
    email = input("email: ")
    cur.execute(f"""insert into Student(name,age,email) values ('{name}','{age}','{email}')""")
    conn.commit()
    cur.close()



def get():
    cur = conn.cursor()
    cur.execute("select * from student;")
    rows = cur.fetchall()       
    conn.commit()
    cur.close()
    for i in rows:
        print(i)
        
def get_by_id():
    cur = conn.cursor()
    ids = int(input("id = "))
    cur.execute(f"select * from student where id = {ids};")
    rows = cur.fetchall()       
    conn.commit()
    cur.close()
    print(rows)
    
    
def update():
    cur = conn.cursor()
    ids = int(input("kadom idiro mekhohed alish kuned: "))
    name = input("New_name: ")
    age = int(input("New_age: "))
    email = input("New_email: ")
    cur.execute(f"update student set name = '{name}',age = '{age}',email = '{email}' where id = {ids}")
    conn.commit()
    cur.close()
    
    
    # for i in rows:
    #     ass = int(input("rakamro vorid kuned: "))
    #     if ass == i:
    #         print(i)
    #     else:
    #         print("rakami nodurust")
def delete():
    cur  = conn.cursor()
    ids = int(input("id = "))
    cur.execute(f"delete from student where id = {ids};")
    conn.commit()
    cur.close()
    print(f"hamin id {ids} nest karda shud!")
while True:
    a = int(input('-> '))
    if a == 1:
        add()
    elif a == 2:
        get()
    elif a == 3:
        get_by_id()
    elif a == 4:
        delete()
    elif a == 5:
        update()
    elif a == 6:
        exit
        
    else:
        print("rakami nodurust")

conn.close()

















# lis = []
# class Student:
#     def __init__(self,name,age,email):
#         self.name = name
#         self.age = age
#         self.email = email
#     def __str__(self):
#         print(self.age,self.email,self.name)

# class Student_meneger:
#     def add():
#         new_lis = Student(
#             name=input("name: "),
#             age=input("age: "),
#             email=input("email: ")
#         )
#         lis.append(new_lis)
#     def edit():
#         print(lis)
#         id = int(input("kadom "))
#         if 
             

