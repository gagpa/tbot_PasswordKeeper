import os

from flask import Flask

from configs import main_configs


def create_app(config_name):
    app = Flask(__name__)
    config = main_configs[config_name]
    app.config.from_object(config)

    from app.tbot_api import api
    app.register_blueprint(api, url_prefix='/api/v1')
    return app


app = create_app(os.environ.get('APP_MODE') or 'default')
