import argparse
from gestures import Gesture
import os
import qi
import sys
from cd import *
from motion import *
from sonar import *

tablet = "./tablet/"
scripts = "scripts"


def handleLastAnswer(lastAnswer):
    if "tablet" in lastAnswer:
        lauch_application(tablet)
    elif "Bye" in lastAnswer:
        print(lastAnswer,"1")


def lauch_application(app):
    with cd(os.path.join(app, scripts)):
        os.system("python demo.py")
    return


def main(session, topic_path):

    # Get ALDialog service
    ALDialog = session.service('ALDialog')
    ALMemory = session.service('ALMemory')
    ALMotion = session.service("ALMotion")
    tts_service = session.service("ALTextToSpeech")

    robot_position = (0,0)

    # Sonar
    sonar = Sonar(ALMemory)
    sonar.set_sonar()

    # Motion
    motion = Motion(ALMotion)
    #min_distance = motion.selectMinDistance(humans_positions) -> prendo la distanza minima tra quelle nel sonar (per il momento solo humans frontali)
    #possiamo fare anche che l'umano sta in diagonale rispetto al robot, questo richiederebbe di calcolare l'angolo alpha tra il robot e l'umano 
    #usando l'arcotangente e far poi ruotare il robot di quell'angolo alpha
    #motion.forward(min_distance, sonar)


    # Gestures
    gesture = Gesture(ALMotion)

    tts_service.setLanguage("English")
    tts_service.setVolume(1.0)
    tts_service.setParameter("speed", 1.0)
    tts_service.say("Hi! I'm MARIO."+" "*5)
    gesture.doHello()
    

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
        try:
            value = raw_input("Talk to robot (insert stop to finish the conversation): ")

        except KeyboardInterrupt:
            stop_flag = True
            # Stop the dialog engine
            ALDialog.unsubscribe('pepper_assistant')
            # Deactivate and unload the main topic
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name)   
            return 0

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