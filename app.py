from flask import Flask  # type: ignore[import-not-found]

app = Flask(__name__)  # створюємо веб-додаток


@app.route("/")
def hello_world():
    return "Hello, Flask!"  # що повернути користувачу


if __name__ == "__main__":
    app.run(debug=True)
