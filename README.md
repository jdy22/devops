# Literature Searcher

To run the app, first prepare the virtual environment:

```shell
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

You can now execute the Gunicorn web server (which is what you would do in _production_) or run
the app directly from Flask: this is what you do during development, as you can benefit from useful
debug logs.

```shell
# Gunicorn (Production)
export PORT=5000
gunicorn --config gunicorn_config.py wsgi:app

# Flask (Development)
flask run
```

Either case, your app will be live at <http://localhost:5000>.
