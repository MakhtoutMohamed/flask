from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")





# please make FLASK_ENV on using this commande on cmd
# export FLASK_ENV=development