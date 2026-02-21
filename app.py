
m flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "Payment Service Online", "version": "1.0.0"})

@app.route('/pay', methods=['POST'])
def pay():
    return jsonify({"message": "Payment processed successfully", "id": "PAY-12345"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
