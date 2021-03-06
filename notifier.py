import smtplib
import MySQLdb as mdb
import datetime
import pytz

from etc import Config


smtp_config = Config.smtp()
db_config = Config.db()

db_conn = mdb.connect(db_config["host"],
                      db_config["user"],
                      db_config["password"],
                      db_config["name"])

to_addresses = []

try:
    query = "SELECT DISTINCT(email) from users"
    db_cursor = db_conn.cursor()
    db_cursor.execute(query)

    results = db_cursor.fetchall()

    if len(results) == 0:
        print "No emails to send"
        exit()

    for row in results:
        to_addresses.append(row[0])

except Exception as e:
    print e.message
    exit()

to_addresses.append(smtp_config["user"])
to_address = ";".join(to_addresses)

birthdays_today = []

try:
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(tz)
    month = now.strftime("%m")
    day = now.strftime("%d")

    query = "SELECT DISTINCT(name) FROM users WHERE MONTH(birthday) = %s AND DAY(birthday) = %s"
    db_cursor = db_conn.cursor()
    db_cursor.execute(query, (month, day))

    results = db_cursor.fetchall()

    if len(results) == 0:
        print "No birthdays today"
        exit()

    for row in results:
        birthdays_today.append(row[0])

except Exception as e:
    print e.message
    exit()


try:
    msg = "\r\n".join([
        "From: " + smtp_config["user"],
        "To: " + to_address,
        "Subject: Birthday Notifications",
        "",
        "Birthdays today: " + ", ".join(birthdays_today)
    ])

    server = smtplib.SMTP_SSL(smtp_config["server"], 465)
    server.ehlo()
    server.login(smtp_config["user"], smtp_config["password"])
    server.sendmail(from_addr=smtp_config["user"], to_addrs=to_addresses, msg=msg)
    server.close()
except Exception as e:
    print e.message
    exit()

