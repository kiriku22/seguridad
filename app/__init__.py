from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_bcrypt import Bcrypt

limiter = Limiter(key_func=get_remote_address)
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt  = Bcrypt()

#crea app
app = Flask(__name__)
app.config.from_object(Config)



db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)
limiter.init_app(app)


# Importar rutas después de crear e inicializar la app
from app import routes