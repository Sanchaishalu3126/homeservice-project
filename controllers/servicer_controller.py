from flask import Blueprint, render_template, request, session
from models.servicer_model import ServicerModel

servicer_bp = Blueprint('servicer', __name__)

@servicer_bp.route("/servicer", methods=["GET", "POST"])
def dashboard():

    servicer = ServicerModel.get_servicer_by_user(session["user_id"])

    if request.method == "POST":
        ServicerModel.create_servicer(
            session["user_id"],
            request.form["service"],
            request.form["proof"]
        )
        servicer = ServicerModel.get_servicer_by_user(session["user_id"])

    booking_count = 0
    if servicer:
        booking_count = ServicerModel.get_booking_count(servicer[0])

    return render_template(
        "servicer_dashboard.html",
        servicer=servicer,
        booking_count=booking_count
    )