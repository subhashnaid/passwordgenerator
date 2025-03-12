from flask import Flask, request, send_from_directory
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate')
def generate():
    length = int(request.args.get('length', 8))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbol = string.punctuation
    all = lower + upper + number + symbol
    temp_password = random.sample(all, length)
    password = "".join(temp_password)
    return password

if __name__ == '__main__':
    app.run(debug=True)