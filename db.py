import sqlite3

def init_db():
    # データベースの初期化を行う関数
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    with open("schema.sql", mode="r") as f:
        sql = f.read()

    cursor.executescript(sql)

    conn.commit()

    conn.close()


def find_all_users():
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()
    sql = "SELECT * FROM customers"
    results = cursor.execute(sql)
    users = results.fetchall()

    conn.commit()
    conn.close()
    return users


def add_user(name, age):
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    sql = "INSERT INTO customers (name,age) VALUES (?,?)"

    cursor.execute(sql, (name, age))

    conn.commit()

    conn.close()


if __name__ == '__main__':
    init_db()