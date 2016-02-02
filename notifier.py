import smtplib

from etc import Config


smtp_config = Config.smtp()

to_address = "somsubhra.bairi@gmail.com;somsubhra.bairi@yahoo.com"

msg = "\r\n".join([
    "From: " + smtp_config["user"],
    "To: " + to_address,
    "Subject: Birthday Notifications",
    "",
    "Test message"
])

server = smtplib.SMTP_SSL(smtp_config["server"], 465)
server.ehlo()
server.login(smtp_config["user"], smtp_config["password"])
server.sendmail(from_addr=smtp_config["user"], to_addrs=to_address, msg=msg)
server.close()
