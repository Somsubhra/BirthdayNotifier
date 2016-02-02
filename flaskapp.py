from flask import Flask, render_template, request
from etc import Config
import MySQLdb as mdb


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
    name = str(request.form["name"])
    email = str(request.form["email"])
    birthday = str(request.form["birthday"])

    if name.strip() != "" and email.strip() != "" and birthday.strip() != "":
        db_config = Config.db()
        db_conn = mdb.connect(db_config["host"],
                              db_config["user"],
                              db_config["password"],
                              db_config["name"])

        db_cursor = db_conn.cursor()

        query = "INSERT IGNORE INTO users(name, email, birthday) VALUES(%s, %s, %s)"

        try:
            db_cursor.execute(query, (name,
                                      email,
                                      birthday))
            db_conn.commit()
        except Exception as e:
            return render_template("form.html", error=e.message)
    else:
        return render_template("form.html", error="All fields are required")

    return render_template("thanks.html")
