from flask import Flask
from aihub.main.controllers import main
from aihub.admin.controllers import admin
from aihub.config.controllers import DevelopmentConfig

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
app.config.from_object(DevelopmentConfig)