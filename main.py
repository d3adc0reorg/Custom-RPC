from helpers.config import set_setting, get_setting
from web_interface import start_web_interface
from pypresence import Presence
from pypresence import exceptions
import threading
import os, sys
import time

os.chdir(sys.path[0])

print('Custom RPC, By Purpl3')

if not os.path.isfile('config.ini'):

    with open('config.ini', 'w') as cfg:cfg.write('[main]') # create config set_setting('state', 'Your Text Here')

    set_setting('large_text', 'Custom RPC') 
    set_setting('start_time_seconds', '60')
    set_setting('button1_label', 'My Button 1')
    set_setting('button1_url', 'https://google.com')
    set_setting('button1_enable', 'true')


    set_setting('button2_url', 'https://google.com')
    set_setting('button2_label', 'My Button 2')
    set_setting('button2_enable', 'true')

    set_setting('web_interface', 'true')

    set_setting('delay', '60')


try:RPC = Presence('1107688443393347604')
except exceptions.DiscordNotFound:
    print('Discord not found!\nMake sure you open Discord (Desktop)')
    quit()

print('Connecting to discord...') 

try: RPC.connect()
except Exception as e: print(f'Error connecting to Discord RPC: ' + str(e)); quit()

print('Done!')

convert_boolean = {'true': True, 'false': False}

cfg_state = str(get_setting('state', if_option_not_exist='Your Text Here'))

cfg_start_time = int(get_setting('start_time_seconds', if_option_not_exist='10'))

cfg_button1_label = str(get_setting('button1_label', if_option_not_exist='My Button 1'))
cfg_button1_url = str(get_setting('button1_url', if_option_not_exist='https://google.com'))
cfg_button1_enable = convert_boolean[str(get_setting('button1_enable', if_option_not_exist='true'))]

cfg_button2_label = str(get_setting('button2_label', if_option_not_exist='My Button 2'))
cfg_button2_url = str(get_setting('button2_url', if_option_not_exist='https://google.com'))
cfg_button2_enable = convert_boolean[str(get_setting('button2_enable', if_option_not_exist='true'))]
cfg_delay = int(get_setting('delay', if_option_not_exist='60'))
cfg_webinterface = convert_boolean[str(get_setting('web_interface', if_option_not_exist='true'))]

if cfg_webinterface:
    threading.Thread(target=start_web_interface).start()

    print('Web interface started: http://localhost:5000')
    
def make_button_dict():
    output = []

    if cfg_button1_enable:
        output.append({'label': cfg_button1_label, 'url': cfg_button1_url})

    if cfg_button2_enable:
        output.append({'label': cfg_button2_label, 'url': cfg_button2_url})

    return output

def update(start_time: int):
    if start_time < -0:
        print('Start time cannot be less than 0!')
        quit()
    
    start_time = time.time() - start_time

    # seconds
    # 3600 - hour
    # 3600/2 = 1800 - 30 minutes
    # 60 - 1 minute

    button_dict = make_button_dict()

    if len(button_dict) == 0:
        RPC.update(
        large_text='None',
        large_image='logo', 
        state=cfg_state,
        start=start_time)

    elif len(button_dict) != 0:
        RPC.update(
        large_text='None',
        large_image='logo', 
        state=cfg_state,
        start=start_time,
        buttons=button_dict)

while True:
    update(cfg_start_time)

    time.sleep(cfg_delay)