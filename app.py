import os
from flask import Flask
from flask_openid import OpenID
from config import Configuration


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

oid = OpenID(app, os.path.join(Configuration.BASEDIR, 'tmp'))
