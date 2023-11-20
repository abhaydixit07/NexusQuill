from flask import Flask,render_template, request
import requests
import smtplib

app=Flask(__name__)
PASSWORD = "pzmyktvgocakvtsb"
EMAIL = "abhaydixitfake@gmail.com"


def send_mail(name, email, phone, message):
    connection=smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)

    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:NexusQuill mail From {name}\n\nName: {name}\nEmail: {email}\nPhone No.:{phone}\n{message}")
    connection.close()
# unsplash for images
# https://www.npoint.io/docs/2e4a0e1ee10447867a0d
response=requests.get("https://api.npoint.io/2e4a0e1ee10447867a0d")
data=response.json()
@app.route('/')
def home():
    return render_template("index.html", posts=data)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method=="POST":
        form_data = request.form
        send_mail(form_data["name"], form_data["email"], form_data["phone"], form_data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

@app.route('/form-entry', methods=["POST"])
def receive_data():
    return "<h1>Suceesss</h1>"

@app.route('/post/<int:num>')
def show_post(num):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__=="__main__":
    app.run(debug=True)

