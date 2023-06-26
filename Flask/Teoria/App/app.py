from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

    def hello():
    return "<h1>Hello World!</h1>"

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)