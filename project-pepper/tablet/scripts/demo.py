import sys
import time
import os
import random

try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print("Please set MODIM_HOME environment variable to MODIM folder.")
    sys.exit(1)

# Set MODIM_IP to connnect to remote MODIM server

import ws_client
from ws_client import *

def i1():

    im.init()
    lan = im.ask('language')

    if lan == "it":
        im.setProfile(['*','*','it','*'])

    im.execute('welcome')
    a0 = im.ask('welcome', timeout=999)
    q = 'interaction'
    a = im.ask(q)

    if (a!='timeout'):
        im.execute(a)
        im.execute('goodbye')

    else:
        q = "color-warning"
        a = im.ask(q)
        if (a!='timeout'):
            im.execute(a)
            im.execute('goodbye')
        else:
            im.execute('goodbye')

    im.init()


if __name__ == "__main__":

    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    # mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')

    mws.run_interaction(i1)


