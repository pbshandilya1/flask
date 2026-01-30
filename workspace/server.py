from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/win/timezone', methods=['POST'])
def handle_request():
    # Your malicious script logic here
    data = request.get_json()
    # Process the request and return a response
    return "Response"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
