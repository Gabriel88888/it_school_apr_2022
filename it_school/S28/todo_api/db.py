def create_todo_table(con):
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS (
    id INTEGER PRIMARY KEY,
    title TEXT NULL,
    body TEXT
    done INTEGER DEFAULT 0
    )
    """)
    con.commit()
#CRUD


# create todo
def create_todo(con, title, body):
    cur = con.cursor()
    cur.execute("""
    INSERT INTO todos (title, body)
    VALUES 
    (?, ?)
    """, (title, body))
    con.commit()
#read todos
def read_todos(con,):
    cur = con.cursor()
    cur.execute("""SELECT * FROM todos""")
    con.commit()



#read todo
def read_todo(con,id):
    cur = con.cursor()
    cur.execute("""SELECT * FROM todos WHERE id=?""", (id,))
    con.commit()

#update todo
def complete_todo(con, id,):
    cur = con.cursor()
    cur.execute("""UPDATE todos SET done=1 WHERE id=?""", (id,))
    con.commit()


#delet todo

def delete_todo(con, id):
    cur = con.cursor()
    cur.execute("""DELETE todos WHERE id=?""", (id,))
    con.commit()