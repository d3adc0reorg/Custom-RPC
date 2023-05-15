from helpers.config import set_setting, get_setting
from web_interface import start_web_interface
from pypresence import Presence
from threading import Thread
import os, sys
import time

os.chdir(sys.path[0])

print('Custom RPC, By Purpl3')

if not os.path.isfile('config.ini'):

    with open('config.ini', 'w') as cfg:cfg.write('[main]') # create config set_setting('state', 'Your Text Here')

    set_setting('large_text', 'Custom RPC') 
    set_setting('start_time', '10')
    set_setting('button1_label', 'My Button 1')
    set_setting('button1_url', 'https://google.com')
    set_setting('button1_enable', 'true')


    set_setting('button2_url', 'https://google.com')
    set_setting('button2_label', 'My Button 2')
    set_setting('button2_enable', 'true')

    set_setting('web_interface', 'true')


RPC = Presence ('1107688443393347604')
print('Connecting to discord...') 

try: RPC.connect()
except Exception as e: print(f'Error connecting to Discord RPC: ' + str(e)); quit()

print('Done!')

convert_boolean = {'true': True, 'false': False}

cfg_state = str(get_setting('state', if_option_not_exist='Your Text Here'))

cfg_start_time = int(get_setting('start_time', if_option_not_exist='10'))

cfg_button1_label = str(get_setting('button1_label', if_option_not_exist='My Button 1'))
cfg_button1_url = str(get_setting('button1_url', if_option_not_exist='https://google.com'))
cfg_button1_enable = convert_boolean[str(get_setting('button1_enable', if_option_not_exist='true'))]

cfg_button2_label = str(get_setting('button2_label', if_option_not_exist='My Button 2'))
cfg_button2_url = str(get_setting('button2_url', if_option_not_exist='https://google.com'))
cfg_button2_enable = convert_boolean[str(get_setting('button2_enable', if_option_not_exist='true'))]

cfg_webinterface = convert_boolean[str(get_setting('web_interface', if_option_not_exist='true'))]

#if cfg_webinterface:
    #Thread(target=start_web_interface()).run()

def make_button_dict():
    output = []

    if cfg_button1_enable:
        output.append({'label': cfg_button1_label, 'url': cfg_button1_url})

    if cfg_button2_enable:
        output.append({'label': cfg_button2_label, 'url': cfg_button2_url})

    return output

def update(start_time: int = 10):
    if start_time < 1:
        return Exception('Start time cannot be less than 1')

    elif start_time > 24:
        return Exception('Start time cannot be more than 24')

    start_time = time.time() - 3600 * start_time

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
print('123')
while True:
    update(cfg_start_time)

    time.sleep(60)