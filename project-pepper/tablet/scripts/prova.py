from naoqi import ALProxy

IP = "127.0.0.1"
tts = ALProxy("ALTextToSpeech", IP, 9559)
#audio = ALProxy("ALAudioDeviceProxy", IP, 9559)
tts.say("Hello world from python")