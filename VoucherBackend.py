import sqlite3


# registered into database
def register_user(uname, passwd):
    con = sqlite3.connect("VirtualVouchers.db")
    cur = con.cursor()
    cur.execute("create table if not exists Login(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password BLOB)")
    # cur.execute("drop table Login")

    # cur.execute("Insert into login(username,password) values('rohit','admin')")
    cur.execute("Insert into login(username,password) values(?,?)", (uname, passwd))

    cur.execute("select * from Login")
    print(cur.fetchall())

    con.commit()
    con.close()


# connect("Rohit", "Rohit03")

def user_login(username, password):
    connetion = sqlite3.connect("VirtualVouchers.db")
    cursor = connetion.cursor()
    insert = "select * from login"
    cursor.execute(insert)
    # print("DATA GOT: -", cursor.fetchall())
    data = cursor.fetchall()
    for i in data:
        if username == i[1] and password == i[2]:
            print("got", username, password, i[1], i[2])
            return True
        # else:
        #     print("NO", username, password, i[1], i[2])

    connetion.commit()
    connetion.close()


# a = user_login("admin", "admin")
# print(a)
