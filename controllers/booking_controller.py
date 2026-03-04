from flask import Blueprint, render_template, request, session, redirect, url_for
from models.servicer_model import ServicerModel
from models.booking_model import BookingModel

booking_bp = Blueprint('booking', __name__)

@booking_bp.route("/customer", methods=["GET", "POST"])
def customer_dashboard():

    if request.method == "POST":
        BookingModel.create_booking(
            session["user_id"],
            request.form["servicer_id"],
            request.form["date"]
        )

    servicers = ServicerModel.get_all_servicers()
    return render_template("customer_dashboard.html", servicers=servicers)

@booking_bp.route("/history")
def history():
    bookings = BookingModel.get_customer_bookings(session["user_id"])
    return render_template("booking_history.html", bookings=bookings)