import sqlite3

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect("database.db", check_same_thread=False)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance.init_db()
        return cls._instance

    def init_db(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT,
                role TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS servicers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                service TEXT,
                proof TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                servicer_id INTEGER,
                date TEXT
            )
        """)

        self.connection.commit()

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor