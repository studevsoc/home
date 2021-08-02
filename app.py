from flask import Flask, render_template, request
import os, smtplib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    mail = f'Name: {name} \n Email: {email} \n Phone: {phone} \n {message}'
    # Mailer
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    email_addr = os.getenv('EMAIL_ADDR')
    email_pass = os.getenv('EMAIL_PASS')
    contact_email = os.getenv('TO_ADDR')
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_addr, email_pass)
    server.sendmail(email_addr, contact_email, mail)
    return render_template("success.html", name=name)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/coc")
def coc():
    return render_template("coc.html")
