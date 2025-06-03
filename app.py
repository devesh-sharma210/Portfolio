from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    my_projects = [
        {
            "title": "Weather App",
            "description": "Shows weather using OpenWeatherMap API",
            "tech": "Python, Flask, API",
            "link": "https://github.com/yourusername/weather-app"
        },
        {
            "title": "ToDo App",
            "description": "Manage tasks with SQLite",
            "tech": "Flask, SQLAlchemy",
            "link": "https://github.com/yourusername/todo-app"
        },
        {
            "title": "Portfolio Website",
            "description": "This portfolio you are viewing now!",
            "tech": "Flask, HTML, CSS",
            "link": "#"
        }
    ]
    return render_template("projects.html", projects=my_projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        subject = f"Message from {name}"
        body = f"From: {name} <{email}>\n\n{message}"

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = email
        msg["To"] = "youremail@example.com"  # CHANGE THIS

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login("youremail@example.com", "your-app-password")  # CHANGE THIS
                server.sendmail(email, "youremail@example.com", msg.as_string())
        except Exception as e:
            print("Error sending email:", e)

        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
