import os

from flask import Flask, render_template, request, flash

from literature_searcher import query_processor

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    @app.route("/")
    def home():
        return render_template("search_page.html")

    @app.route("/search_result", methods=["GET", "POST"])
    def response():
        query = request.args["search_query"]
        if not query:
            flash("No query")
        search_results = query_processor.process(query)
        return render_template("search_result.html", search_results=search_results)
    return app