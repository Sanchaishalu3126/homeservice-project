from models.database import Database
db = Database()

class ServicerModel:

    @staticmethod
    def create_servicer(user_id, service, proof):
        db.execute(
            "INSERT INTO servicers (user_id, service, proof) VALUES (?, ?, ?)",
            (user_id, service, proof)
        )

    @staticmethod
    def get_servicer_by_user(user_id):
        return db.execute(
            "SELECT * FROM servicers WHERE user_id=?",
            (user_id,)
        ).fetchone()

    @staticmethod
    def get_all_servicers():
        return db.execute("""
            SELECT servicers.id, users.name, service
            FROM servicers
            JOIN users ON users.id = servicers.user_id
        """).fetchall()

    @staticmethod
    def get_booking_count(servicer_id):
        return db.execute(
            "SELECT COUNT(*) FROM bookings WHERE servicer_id=?",
            (servicer_id,)
        ).fetchone()[0]