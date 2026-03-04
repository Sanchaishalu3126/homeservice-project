from models.database import Database
db = Database()

class BookingModel:

    @staticmethod
    def create_booking(customer_id, servicer_id, date):
        db.execute(
            "INSERT INTO bookings (customer_id, servicer_id, date) VALUES (?, ?, ?)",
            (customer_id, servicer_id, date)
        )

    @staticmethod
    def get_customer_bookings(customer_id):
        return db.execute("""
            SELECT users.name, servicers.service, bookings.date
            FROM bookings
            JOIN servicers ON servicers.id = bookings.servicer_id
            JOIN users ON users.id = servicers.user_id
            WHERE bookings.customer_id=?
        """, (customer_id,)).fetchall()