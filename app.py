from flask import Flask, render_template, request
import os, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def success():
    # Get data from the form
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    phone = request.form.get("phone")
    text = request.form.get("message")

    # Format the mail body
    message = "Name: {} \nEmail: {} \nPhone: {} \n{}".format(name, email, phone, text)

    # Configure mail headers
    mail = MIMEMultipart()
    mail["From"] = "admin@studevsoc.com"
    mail["To"] = "contact@studevsoc.com"
    mail["Subject"] = subject
    mail["Cc"] = email
    msg = MIMEText(message, "plain")
    mail.attach(msg)

    # information to connect to the mail server
    smtp_server = "smtp.purelymail.com"
    smtp_port = 587
    email_addr = "admin@studevsoc.com"
    email_pass = os.getenv("EMAIL_PASS")
    contact_email = "contact@studevsoc.com"

    # Connect to the Mail server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_addr, email_pass)
    server.sendmail(email_addr, contact_email, mail.as_string())

    # Let the user know that the transaction was successful
    return render_template("success.html", name=name)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/coc")
def coc():
    return render_template("coc.html")
