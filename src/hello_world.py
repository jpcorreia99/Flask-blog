from flask import Flask

app = Flask(__name__)  # __name__ referencia o ficheiro


@app.route("/")
@app.route("/home")  # tanto a root como a página home executam esta função
def hello():
    return "Home page"


if __name__ == "__main__":
    app.run(debug=True)  # atcually shows the errors and not just the codes
