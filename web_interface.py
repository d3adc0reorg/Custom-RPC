from flask import Flask, render_template, send_file
from helpers.config import get_items, get_setting
import logging


app = Flask(__name__, template_folder='webinterface/templates')

app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

def start_web_interface():
    @app.route('/')
    def index():
        settings = get_items()

        for setting in settings:
            
            if setting[0] == 'state':
                state = setting[1]

            elif setting[0] == 'start_time':
                start_time = setting[1]

            elif setting[0] == 'button1_enable':
                if setting[1] == 'true':
                    button1_label = get_setting('button1_label')
                    button1_url = get_setting('button1_url')
                    button1_enable = 'true'
                else:
                    button1_label = 'none'
                    button1_url = 'none'
                    button1_enable = 'false'

            elif setting[0] == 'button2_enable':
                if setting[1] == 'true':
                    button2_label = get_setting('button2_label')
                    button2_url = get_setting('button2_url')
                    button2_enable = 'true'
                else:
                    button2_label = 'none'
                    button2_url = 'none'
                    button2_enable = 'false'


        return render_template('index.html', settings=settings, state=state, start_time=start_time,
                               button1_enable=button1_enable,
                               button1_label=button1_label,
                               button1_url=button1_url,
                               
                               button2_enable=button2_enable,
                               button2_label=button2_label,
                               button2_url=button2_url)

    @app.route('/logo')
    def get_logo():
        return send_file('webinterface/static/logo.png')

    app.run('localhost', 5000, debug=False)

#start_web_interface()