from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/do_login", methods=["POST"])
def do_login():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
