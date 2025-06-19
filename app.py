from flask import Flask, render_template, request
from converters import Decimal, Binary, Hexadecimal

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        number = request.form.get("number")
        conversion = request.form.get("conversion")

        try:
            if conversion == "to_bin":
                result = Decimal.to_bin(int(number))
            elif conversion == "to_hex":
                result = Decimal.to_hex(int(number))
            elif conversion == "to_dec_from_bin":
                result = Binary.to_dec(number)
            elif conversion == "to_hex_from_bin":
                result = Binary.to_hex(number)
            elif conversion == "to_dec_from_hex":
                result = Hexadecimal.to_dec(number)
            elif conversion == "to_bin_from_hex":
                result = Hexadecimal.to_bin(number)
        except ValueError as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)