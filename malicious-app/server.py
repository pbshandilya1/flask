from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Service is running"})

@app.route('/win/timezone', methods=['POST'])
def handle_request():
    data = request.get_json()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
