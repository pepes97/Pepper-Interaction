import argparse
import os
import qi
import sys
from cd import *
from motion import *


tablet = "./tablet/"
scripts = "scripts"

def handleLastAnswer(lastAnswer):
    if "tablet" in lastAnswer:
        lauch_application(tablet)

def lauch_application(app):
    with cd(os.path.join(app, scripts)):
        os.system("python demo.py")
    return

def main(session, topic_path):
    # Get ALDialog service
    ALDialog = session.service('ALDialog')
    ALMemory = session.service('ALMemory')
    ALMotion = session.service("ALMotion")

    motion = Motion(ALMotion)
    motion.forward()

    # Setup ALDialog
    ALDialog.setLanguage('English')
    
    topic_path += "/main.top"

    # Loading the topic given by the user (absolute path is required)
    topf_path = topic_path.decode('utf-8')
    topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

    # Activate loaded topic
    ALDialog.activateTopic(topic_name)

    # Black magic
    lastAnswer = ALMemory.subscriber("Dialog/LastAnswer")
    lastAnswer.signal.connect(handleLastAnswer)

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

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")
    parser.add_argument("--topic-path", type=str, required=True,
                        help="absolute path of the dialog topic folder")


    args = parser.parse_args()
    session = qi.Session()

    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    
    main(session, args.topic_path)