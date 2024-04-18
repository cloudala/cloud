from flask import Flask

port = 8080

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)