from flask import Flask, render_template, request
from etc import Config


app = Flask(__name__)
app.config.update(
    DEBUG=Config.debug(),
    PROPAGATE_EXCEPTIONS=Config.propagate_exceptions(),
    SECRET_KEY=Config.secret_key(),
    HOST_NAME=Config.host_name(),
    APP_NAME=Config.app_name(),
    IP=Config.ip(),
    PORT=Config.port()
)


@app.route("/")
def form_handler():
    return render_template("form.html")


@app.route("/save", methods=["POST"])
def save_handler():
    name = request.form["name"]
    email = request.form["email"]
    birthday = request.form["birthday"]

    return render_template("thanks.html")
