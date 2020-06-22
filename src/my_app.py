from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # __name__ referencia o ficheiro

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == "__main__":
    app.run(debug=True)  # atcually shows the errors and not just the codes

# Nota: ps -fA | grep python e kill do pid para terminar outros flasks
