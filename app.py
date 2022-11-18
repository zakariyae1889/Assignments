from flask import  Flask
import os
from WebSite.Data.data import DataConnect
from WebSite.routes.view import view
def create_app():
    app=Flask(__name__)
    app.secret_key=os.urandom(150)
    DataConnect()
    app.register_blueprint(view,url_prefix="/")
    return app