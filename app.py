from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['number1'])
    num2 = float(request.form['number2'])
    result = num1 + num2
    return jsonify({'answer': result})

if __name__ == '__main__':
    app.run(debug=True)
