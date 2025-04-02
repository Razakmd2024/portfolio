from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY']="@2025"
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0
app.config['TIMEOUT']=300 

# Create a file counter.txt and initialize it with 0
def get_visitor_count():
    try:
        with open("counter.txt","r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def increment_visitor_count():
    count = get_visitor_count() + 1
    with open("counter.txt","w") as file:
        file.write(str(count))
    return count




@app.route("/", methods=['GET'])
def home():
    count = increment_visitor_count()
    return render_template("home.html", visitor_count = count)

@app.route("/about", methods=['GET'])
def About():
    return render_template("about.html")

@app.route("/contact", methods=['GET'])
def contact():
    return render_template("contact.html")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
@app.route("/projects")
def project():
    return render_template("project.html")


if __name__ == "__main__":
    app.run(debug=True)