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

    q = 'choose-activity'
    a = im.ask(q)
    while a != "exit":
        if a == "meteo":
            q = "choose-" + str(random.choice(["sunny", "cloudy", "snow", "stormy", "foggy", "rainy", "windy"]))
            a = im.ask(q)
            if a == "back":
                a = im.ask("choose-activity")

        elif a == "news":
            while a != "back":
                a = im.ask("choose-topic")

                if a == "politics":
                    im.ask("choose-politics")
                elif a == "sport":
                    im.ask("choose-sport")
                elif a == "health":
                    im.ask("choose-health")
                elif a == "science":
                    im.ask("choose-science")    
                elif a == "entertainment":
                    im.ask("choose-entertainment")
            
            a = im.ask("choose-activity")


    im.execute('goodbye')
    
    #im.init()




if __name__ == "__main__":

    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    # mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')

    mws.run_interaction(i1)


