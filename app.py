from flask import Flask, render_template, request
from converters import Decimal, Binary, Hexadecimal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)