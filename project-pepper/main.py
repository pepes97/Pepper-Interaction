from __future__ import division

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
from numpy.random import choice

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

def getTypeImage(index):
    
    counter_class = database.patients[name]["music"][index][0]
    counter_tot = 0
    for i in range(len(database.patients[name]["music"])):
        counter_tot += database.patients[name]["music"][i][0]

    weight_happy = counter_class/counter_tot if counter_tot!=0 else 0
    print(weight_happy)

    l = [weight_happy/2, (1-weight_happy)/2, (1-weight_happy)/2, weight_happy/2]
    print(l, sum(l))

    if weight_happy != 0:
        return choice(["happyImage", "neutralImage", "sadImage", "surpriseImage"], 1, p=[weight_happy/2, (1-weight_happy)/2, (1-weight_happy)/2, weight_happy/2])[0]
    else:
        return choice(["happyImage", "neutralImage", "sadImage", "surpriseImage"], 1)[0]

    

def handleLastAnswer(lastAnswer):
    global name
    global topic_name

    audio_player_service = session.service("ALAudioPlayer")
    selected_index = str(random.choice([1,2,3]))

    print(lastAnswer)

    if "start" in lastAnswer:
        lauch_application(tablet)
    elif "bye" in lastAnswer:
        print(lastAnswer,"1")
    elif "Hi" in lastAnswer:
        name = lastAnswer.split()[1]
        if name.lower() not in database.patients:
            database.addPatient(name.lower())
            tts_service.say("Nice to meet you!\nDo you want to use the tablet?"+" "*5, _async=True)
        else:

            if max(database.patients[name]["music"])[0] > 0:
                favourite_music_genre = max(database.patients[name]["music"])[1]

                ALDialog.unsubscribe('pepper_assistant')
                ALDialog.deactivateTopic(topic_name)
                ALDialog.unloadTopic(topic_name)  

                if favourite_music_genre == "rock":
                    topic_path = project_path + "/topicFiles/main_rock.top"
                elif favourite_music_genre == "pop":
                    topic_path = project_path + "/topicFiles/main_pop.top"
                elif favourite_music_genre == "classical":
                    topic_path = project_path + "/topicFiles/main_classical.top"
                elif favourite_music_genre == "jazz":
                    topic_path = project_path + "/topicFiles/main_jazz.top"

                # Loading the topic given by the user (absolute path is required)
                topf_path = topic_path.decode('utf-8')
                topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

                # Activate loaded topic
                ALDialog.activateTopic(topic_name)

                # Start dialog
                ALDialog.subscribe('pepper_music_profiled')

            tts_service.say("Welcome back!\nDo you want to use the tablet?"+" "*5, _async=True)
    
    elif "play Classical music ! !" in lastAnswer:
        audio_player_service.playFile(project_path+"/tablet/sounds/classical/classical"+selected_index+".wav", _async=True)
        database.patients[name]["music"][0] = (database.patients[name]["music"][0][0]+1, database.patients[name]["music"][0][1])


        gesture.typeImage = getTypeImage(0)

        gesture.doGesture = True
        gesture.favourite = "classical"
        gesture.doClassical()

    elif "play Pop music ! !" in lastAnswer:
        audio_player_service.playFile(project_path+"/tablet/sounds/pop/pop"+selected_index+".wav", _async=True)
        database.patients[name]["music"][1] = (database.patients[name]["music"][1][0]+1, database.patients[name]["music"][1][1])


        gesture.typeImage = getTypeImage(1) 

        gesture.doGesture = True
        gesture.favourite = "pop"
        gesture.doPop()

    elif "play Rock music ! !" in lastAnswer:
        audio_player_service.playFile(project_path+"/tablet/sounds/rock/rock"+selected_index+".wav", _async=True)
        database.patients[name]["music"][2] = (database.patients[name]["music"][2][0]+1, database.patients[name]["music"][2][1])

        gesture.typeImage = getTypeImage(2)

        gesture.doGesture = True
        gesture.favourite = "rock"
        gesture.doRock()

    elif "play Jazz music ! !" in lastAnswer:
        audio_player_service.playFile(project_path+"/tablet/sounds/jazz/jazz"+selected_index+".wav", _async=True)
        database.patients[name]["music"][3] = (database.patients[name]["music"][3][0]+1, database.patients[name]["music"][3][1])

        gesture.typeImage = getTypeImage(3)

        gesture.doGesture = True
        gesture.favourite = "jazz"
        gesture.doJazz()
        
            


def handleLastInput(lastInput):
    global audio_player_service
    global name
    global doGesture
    global index

    audio_player_service = session.service("ALAudioPlayer")
    selected_index = str(random.choice([1,2,3]))

    if "classical" in lastInput.lower():
        audio_player_service.playFile(project_path +"/tablet/sounds/classical/classical"+selected_index+".wav", _async=True)

        gesture.typeImage = getTypeImage(0)
        
        if max(database.patients[name]["music"])[0] > 0:
            gesture.favourite = max(database.patients[name]["music"])[1]

        database.patients[name]["music"][0] = (database.patients[name]["music"][0][0]+1, database.patients[name]["music"][0][1])
        print(database.patients[name]["music"][0])
        gesture.doGesture = True
        gesture.doClassical()
    
    elif "pop" in lastInput.lower():
        audio_player_service.playFile(project_path +"/tablet/sounds/pop/pop"+selected_index+".wav", _async=True)

        gesture.typeImage = getTypeImage(1)
        
        if max(database.patients[name]["music"])[0] > 0:
            gesture.favourite = max(database.patients[name]["music"])[1]

        database.patients[name]["music"][1] = (database.patients[name]["music"][1][0]+1, database.patients[name]["music"][1][1])
        print(database.patients[name]["music"][1])
        gesture.doGesture = True
        gesture.doPop()

    elif "rock" in lastInput.lower():
        audio_player_service.playFile(project_path+"/tablet/sounds/rock/rock"+selected_index+".wav", _async=True)

        gesture.typeImage = getTypeImage(2)
        
        if max(database.patients[name]["music"])[0] > 0:
            gesture.favourite = max(database.patients[name]["music"])[1]

        database.patients[name]["music"][2] = (database.patients[name]["music"][2][0]+1, database.patients[name]["music"][2][1])
        gesture.doGesture = True
        gesture.doRock()

    elif "jazz" in lastInput.lower():
        audio_player_service.playFile(project_path + "/tablet/sounds/jazz/jazz"+selected_index+".wav", _async=True)

        gesture.typeImage = getTypeImage(3)
        
        if max(database.patients[name]["music"])[0] > 0:
            gesture.favourite = max(database.patients[name]["music"])[1]

        database.patients[name]["music"][3] = (database.patients[name]["music"][3][0]+1, database.patients[name]["music"][3][1])
        gesture.doGesture = True
        gesture.doJazz()
    

    elif "stop" in lastInput.lower():
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
    gesture = Gesture(ALMotion, doGesture, vision, tts_service, )
    touch = Touch(ALMemory)

    # Database
    database = Database()

    main(session)