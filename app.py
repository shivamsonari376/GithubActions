from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Shivam's Flask Calculator API!"

@app.route('/add', methods=['GET'])
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a - b})

@app.route('/multiply', methods=['GET'])
def multiply():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a * b})

@app.route('/divide', methods=['GET'])
def divide():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 1))  # Prevent division by zero
    if b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    return jsonify({'result': a / b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
