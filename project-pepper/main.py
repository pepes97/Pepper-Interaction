import argparse
import os
import qi
import sys
from cd import *

topicContent = ("topic: ~example-assistant()\n"
                "language: enu\n"
                "concept: (myname) [My name is I'm ]\n"
                "proposal: %question Do you want to interact with me?\n"
                    "u1: (yes) Ok, Let's start with my tablet\n"
                    "u2: (no) Ok, What do you want to do?\n"
                "proposal: %name What's your name?\n"
                    "u1: (~myname _*) Nice to meet you $1 ^goto(question)\n"
                "u:([hi hello]) Hi, I'm MARIO ^goto(name)\n")

tablet = "./tablet/"
scripts = "scripts"

def lauch_application(app):
    with cd(os.path.join(app, scripts)):
        os.system("python demo.py")
    return

def main(session):
    # Get ALDialog service
    ALDialog = session.service('ALDialog')

    # Setup ALDialog
    ALDialog.setLanguage('English')
    topic_name = ALDialog.loadTopicContent(topicContent)

    # Activate loaded topic
    ALDialog.activateTopic(topic_name)

    # Start dialog
    ALDialog.subscribe('pepper_assistant')

    stop_flag = False
    while not stop_flag:
        value = raw_input("Talk to robot (insert stop to finish the conversation): ")
        print(value)
        if value =="stop":
            
            stop_flag = True
            # Stop the dialog engine
            ALDialog.unsubscribe('pepper_assistant')
            # Deactivate and unload the main topic
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name)    
        elif "tablet" in value:
            lauch_application(tablet)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()

    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    
    main(session)