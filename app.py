from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Scan Kumar")

@app.route("/subjects")
def subjects():
    return render_template("subjects.html", title="Subjects")


@app.route("/login")
def login():
    return render_template("login.html", title="login")


@app.route("/dashboard")
def dashboard():
    return render_template("admin_dashboard.html", title="Dashboard")


@app.route("/review")
def review():
    return render_template("admin_sub_review.html", title="Review Submission")



if __name__ == '__main__':
    app.run(debug=True)