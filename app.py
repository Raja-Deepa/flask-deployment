from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/")
def index():
    return "Welcome to my Flask application!"

@app.route("/")
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = [str(x) for x in data if str(x).isdigit()]
    alphabets = [str(x) for x in data if str(x).isalpha()]
    highest_alphabet = max(alphabets, key=str.lower, default='')

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)

