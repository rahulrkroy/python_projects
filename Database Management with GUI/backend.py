import sqlite3

def createTable():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id Integer Primary Key, title TEXT, author TEXT,year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",[title,author,year,isbn])
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows=cursor.fetchall()
    conn.close()
    return rows

def search(title='',author='',year='',isbn=''):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",[title,author,year,isbn])
    rows=cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?",[id])
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year =?, isbn=? WHERE id = ?",[title,author,year,isbn,id])
    conn.commit()
    conn.close()


createTable()

# insert("the sky","david",2008,987675345)
# insert("the river","david",2008,987675345)
# update(2,"the river","joker jol",2009,547675345)
# delete(1)
# print(view())
# print(search(year=2008))
