from flask import Flask, jsonify, request

app = Flask(__name__)
userdetails = [
    {
        "Firstname": "Sarada",
        "Lastname": "Barik",
    },
    
]
@app.route('/users')
def home():
    return jsonify(userdetails)

@app.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    userdetails.append(user)
    return jsonify(userdetails)

if __name__ == '__main__':
  app.run(debug=True)




