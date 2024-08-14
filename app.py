from flask import Flask, render_template, request, redirect
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

# Ensure the images folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

subjectlist = [
    ["Engineering chemistry (BCHY101L)", "17 questions available"],
    ["Engineering Physics (BPHY101L)", "17 questions available"]
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Scan Kumar")

@app.route("/subjects", methods=['GET'])
def subjects():
    return render_template("subjects.html", title="Subjects", subjects=subjectlist)

@app.route("/techeng")
def techeng():
    return render_template("questions.html", title="Subjects")

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/forum")
def forum():
    return render_template("forum.html", title="forum")

@app.route("/review", methods=['POST'])
def review():
     if request.method == 'POST':
        if 'file' not in request.files:
            print("File not in request file")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print("File is empty")
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            print(f"Processing file: {filepath}")
            text = pytesseract.image_to_string(Image.open(filepath))
            print(f"Extracted text: {text}")
            #os.remove(filepath)  # Clean up the uploaded file after processing
            option = request.form.get('options')
     return render_template("admin_sub_review.html", title="Review Submission", sem=option,extracted_text=text)

@app.route('/submit', methods=['POST'])
def submit():
    information = request.form
    return render_template("submit.html", data=information)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("admin_dashboard.html", title="Upload Image")

if __name__ == '_main_':
    app.run(debug=True)