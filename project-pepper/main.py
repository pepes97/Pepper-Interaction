import argparse
from gestures import Gesture
from vision import Vision
from touch import Touch
import os
import qi
import sys
from cd import *
from motion import *
from sonar import *
import random
import operator
from database import Database

tablet = "./tablet/"
scripts = "scripts/"

global session
global index
global database
index = 1

global ALDialog
global topic_name
global topic_path
global doGesture
global name


doGesture = True
name = ""

def handleLastAnswer(lastAnswer):
    global name
    if "start" in lastAnswer:
        lauch_application(tablet)
    elif "bye" in lastAnswer:
        print(lastAnswer,"1")
    elif "Hi" in lastAnswer:
        name = lastAnswer.split()[1]
        if name.lower() not in database.patients:
            database.addPatient(name.lower())
            tts_service.say("Nice to meet you! Tell me 'init' to begin the interaction"+" "*5, _async=True)
        else:
            tts_service.say("Welcome back ! Tell me 'init' to begin the interaction"+" "*5, _async=True)

def handleLastInput(lastInput):
    global audio_player_service
    global name
    global doGesture
    global index

    audio_player_service = session.service("ALAudioPlayer")
    selected_index = str(random.choice([1,2,3]))

    if "classical" in lastInput:
        audio_player_service.playFile(project_path +"Pepper-Interaction/project-pepper/tablet/sounds/classical/classical"+selected_index+".wav", _async=True)
        gesture.doGesture = True
        gesture.doClassical()

    
    elif "pop" in lastInput:
        audio_player_service.playFile(project_path +"/tablet/sounds/pop/pop"+selected_index+".wav", _async=True)
        gesture.doGesture = True
        gesture.doPop()


    elif "rock" in lastInput:
        audio_player_service.playFile(project_path+"/tablet/sounds/rock/rock"+selected_index+".wav", _async=True)
        gesture.doGesture = True
        gesture.doRock()


    elif "jazz" in lastInput:
        audio_player_service.playFile(project_path + "/tablet/sounds/jazz/jazz"+selected_index+".wav", _async=True)
        gesture.doGesture = True
        gesture.doJazz()
    

    elif "stop" in lastInput:
        for i in range(1000):
            audio_player_service.stop(i)
        gesture.doGesture = False
        index += 1    


def lauch_application(app):
    with cd(os.path.join(app, scripts)):
        os.system("python demo.py --user "+name)
    return


def main(session):
    stop_flag = False

    # Get ALDialog service
    
    robot_position = (0,0)

    # Sonar
    sonar = Sonar(ALMemory, robot_position)
    sonar.set_sonar()

    # Motion
    motion = Motion(ALMotion)
    #min_distance = motion.selectMinDistance(humans_positions) -> prendo la distanza minima tra quelle nel sonar (per il momento solo humans frontali)
    #possiamo fare anche che l'umano sta in diagonale rispetto al robot, questo richiederebbe di calcolare l'angolo alpha tra il robot e l'umano 
    #usando l'arcotangente e far poi ruotare il robot di quell'angolo alpha
    #motion.forward(min_distance, sonar)
    distances = sonar.get_distances()
    print("Distances: ", distances)
    min_distance, id = motion.selectMinDistance(distances) #id is the person id
    print("Min distance: ", min_distance)
    motion.forward(sonar, min_distance)
    print("Robot position", sonar.robot_position)
    sonar.robot_position = tuple(map(operator.sub, sonar.humans_positions[id], (0.5, 0)))
    print("Robot position", sonar.robot_position)

    tts_service.setLanguage("English")
    tts_service.setVolume(1.0)
    tts_service.setParameter("speed", 1.0)
    tts_service.say("Hello! I'm MARIO.\nI'm here to inform and help you.\nYou can talk with me or interact by clicking the tablet."+" "*5, _async=True)
    gesture.doHello()
    time.sleep(2)

    
    ALDialog.activateTopic(topic_name)
    ALDialog.subscribe('pepper_assistant')

    # Black magic
    lastAnswer = ALMemory.subscriber("Dialog/LastAnswer")
    
    lastAnswer.signal.connect(handleLastAnswer)

    # Black magic 2
    lastInput = ALMemory.subscriber("Dialog/LastInput")
    lastInput.signal.connect(handleLastInput)


    
    while not stop_flag:
        try:
            value = raw_input("Talk to robot (insert stop to finish the conversation) or touch him (LHand, RHand, HeadMiddle): ")

        except KeyboardInterrupt:

            stop_flag = True
            # Stop the dialog engine
            ALDialog.unsubscribe('pepper_assistant')
            # Deactivate and unload the main topic
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name)   
            
            return 0

        if value == "stop":
            
            stop_flag = True
            # Stop the dialog engine
            ALDialog.unsubscribe('pepper_assistant')
            # Deactivate and unload the main topic
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name)    

        elif value == "LHand":
            if touch.isTouched("LHand"):
                tts_service.say("?"+" "*5, _async=True)    
        
        elif value == "RHand":
            if touch.isTouched("RHand"):
                tts_service.say("?"+" "*5, _async=True)   

        elif value == "HeadMiddle":
            if touch.isTouched("HeadMiddle"):
                tts_service.say("?"+" "*5, _async=True)     

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")
    parser.add_argument("--project-path", type=str, required=True,
                        help="path of the project folder, for instance: /home/sveva/playground/Pepper-Interaction/project-pepper")
   
    args = parser.parse_args()
    session = qi.Session()

    project_path = args.project_path

    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)

    ALDialog = session.service('ALDialog')
    ALMemory = session.service('ALMemory')
    ALMotion = session.service("ALMotion")
    tts_service = session.service("ALTextToSpeech")

    # Setup ALDialog
    ALDialog.setLanguage('English')
    
    
    topic_path = project_path + "/topicFiles/main.top"

    # Loading the topic given by the user (absolute path is required)
    topf_path = topic_path.decode('utf-8')
    topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

    # Activate loaded topic
    ALDialog.activateTopic(topic_name)

    # Start dialog
    ALDialog.subscribe('pepper_assistant')

    # Gestures and Vision
    vision = Vision()
    gesture = Gesture(ALMotion, doGesture, vision, tts_service)
    touch = Touch(ALMemory)

    # Database
    database = Database()

    main(session)