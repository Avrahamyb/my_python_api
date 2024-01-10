from flask import Flask, jsonify

app = Flask(__name__)

data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'Example City'
    }

    

@app.route('/')
def hello():
    return jsonify(data)


if __name__ == '__main__':
    app.run()
