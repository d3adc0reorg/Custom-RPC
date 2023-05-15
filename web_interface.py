from flask import Flask, render_template
from helpers.config import get_items
import logging

app = Flask(__name__, template_folder='webinterface/templates')

app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

def start_web_interface():
    @app.route('/')
    def index():
        settings = get_items()

        return render_template('index.html', settings=settings)

    app.run('localhost', 5000, debug=False)