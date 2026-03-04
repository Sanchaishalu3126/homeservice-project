from flask import Flask
from controllers.user_controller import user_bp
from controllers.servicer_controller import servicer_bp
from controllers.booking_controller import booking_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.register_blueprint(user_bp)
app.register_blueprint(servicer_bp)
app.register_blueprint(booking_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)