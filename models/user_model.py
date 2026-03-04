from models.database import Database
db = Database()

class UserModel:

    @staticmethod
    def register(name, email, password):
        db.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )

    @staticmethod
    def login(email, password):
        return db.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        ).fetchone()

    @staticmethod
    def update_role(user_id, role):
        db.execute(
            "UPDATE users SET role=? WHERE id=?",
            (role, user_id)
        )

    @staticmethod
    def get_user(user_id):
        return db.execute(
            "SELECT * FROM users WHERE id=?",
            (user_id,)
        ).fetchone()