from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response_message = f"Echo: {user_message}"  # Replace this with actual bot logic
    return jsonify(reply=response_message)

if __name__ == '__main__':
    app.run(debug=True)
