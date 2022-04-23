from flask import Flask, render_template
from matplotlib.pyplot import title
app = Flask(__name__)

@app.route("/")
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)

@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)




# please make FLASK_ENV on using this commande on cmd
# export FLASK_ENV=development