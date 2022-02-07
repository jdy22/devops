import os

from flask import Flask, render_template, request, flash


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    from literature_searcher import views

    app.register_blueprint(views.bp)

    return app
