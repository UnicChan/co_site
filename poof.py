from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('home.html', title = "Test")

@app.route("/index")
def index():
    return render_template('index.html', title = "index")

@app.route("/tekst")
def itekst():
    return render_template('tekst.html', title = "tekst")

if __name__=="__main__":
    app.run(debug=True)