# Number Converter

A simple web application for converting numbers between decimal, binary, and hexadecimal formats. Built with Flask, this tool provides an easy-to-use interface for performing various number system conversions.

## Features
- Convert decimal to binary and hexadecimal
- Convert binary to decimal and hexadecimal
- Convert hexadecimal to decimal and binary
- User-friendly web interface
- Input validation and error handling

## How It Works
- Enter a number in the input field
- Select the desired conversion type
- Click "Convert" to see the result

## Conversion Types Supported
- Decimal to Binary
- Decimal to Hexadecimal
- Binary to Decimal
- Binary to Hexadecimal
- Hexadecimal to Decimal
- Hexadecimal to Binary

## Usage
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000/`

## Project Structure
- `app.py`: Main Flask application
- `converters.py`: Conversion logic for decimal, binary, and hexadecimal
- `templates/index.html`: Web interface
- `static/style.css`: Stylesheet

## License
MIT

