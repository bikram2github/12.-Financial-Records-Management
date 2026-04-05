import sqlite3


def get_connection():
    return sqlite3.connect("financial_db.db")


def db_cursor():
    conn = get_connection()
    return conn.cursor()

def create_users_table():
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """)



def create_db_table():
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS financial_records (
            tran_id TEXT NOT NULL,
            amount REAL NOT NULL,
            record_type TEXT NOT NULL,
            category TEXT NOT NULL,
            note TEXT ,
            date TEXT DEFAULT CURRENT_TIMESTAMP
            
        );
        """

        cur.execute(create_table_query)


def insert_record(tran_id, amount, record_type, category, note=None):
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        insert_query = """
        INSERT INTO financial_records (tran_id,amount, record_type, category, note)
        VALUES (?, ?, ?, ?, ?);
        """

        cur.execute(insert_query, (tran_id, amount, record_type, category, note))


def get_all_records():
    with sqlite3.connect("financial_db.db") as conn:
        conn.row_factory = sqlite3.Row  

        cur = conn.cursor()
        cur.execute("SELECT * FROM financial_records;")

        records = cur.fetchall()

        return [dict(row) for row in records]


def get_records_by_date(date):
    with sqlite3.connect("financial_db.db") as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM financial_records WHERE date=?;", (date,)
        ).fetchall()
        return [dict(row) for row in rows]
    

def get_by_category(category):
    with sqlite3.connect("financial_db.db") as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM financial_records WHERE category=?;", (category,)
        ).fetchall()
        return [dict(row) for row in rows]
    

def get_by_type(record_type):
    with sqlite3.connect("financial_db.db") as conn:
        conn.row_factory = sqlite3.Row

        rows = conn.execute(
            "SELECT * FROM financial_records WHERE record_type=?;",
            (record_type,)
        ).fetchall()

        return [dict(row) for row in rows]
    

def sort_records(sort_by):
    if sort_by not in ["date", "amount"]:
        raise ValueError("Invalid sort field")

    with sqlite3.connect("financial_db.db") as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            f"SELECT * FROM financial_records ORDER BY {sort_by};"
        ).fetchall()

        return [dict(row) for row in rows]


def delete_record(record_id):
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        cur.execute("DELETE FROM financial_records WHERE tran_id=?;", (record_id,))
        return cur.rowcount > 0


def update_record(record_id, updated_data):
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        allowed_fields = {"amount", "record_type", "category", "date", "note"}

        filtered_data = {k: v for k, v in updated_data.items() if k in allowed_fields}
        if not filtered_data:
            return False
        set_clause = ", ".join([f"{key} = ?" for key in filtered_data.keys()])
        values = list(filtered_data.values())
        values.append(record_id)

        update_query = f"UPDATE financial_records SET {set_clause} WHERE tran_id = ?;"
        cur.execute(update_query, values)
        return cur.rowcount > 0



def delete_table():
    with sqlite3.connect("financial_db.db") as conn:
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS financial_records;")

