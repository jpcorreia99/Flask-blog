from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)  # __name__ referencia o ficheiro

ENV = 'deploy'

if ENV == 'dev':
    app.debug = True
    app.config.from_pyfile('dev_config.py')

elif ENV == 'deploy':
    app.debug = False
    app.config.from_pyfile('deploy_config.py')

db = SQLAlchemy(app)
from views import *

if __name__ == "__main__":
    app.run()


# Nota: ps -fA | grep python e kill do pid para terminar outros flasks
