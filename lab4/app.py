from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def firstHello():
    return "Hello World!"


@app.route("/localhost:5000/api/v1/hello-world-8")
def hello():
    return "<h2 style='color:green'>Hello World! 8</h2>"


if __name__ == "__main__":
    app.run(debug=True)
