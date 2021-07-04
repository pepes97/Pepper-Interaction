
import time
import math

class Motion:
    def __init__(self, motion_service):
        self.motion_service = motion_service


    def setSpeed(self, lin_vel, ang_vel, dtime, sonar):
        self.motion_service.move(lin_vel, 0, ang_vel)
        time.sleep(dtime)
        self.motion_service.stopMove()
        return 

    def forward(self, sonar, s, lin_vel=0.2, ang_vel=0):
        print("Sonar Values", sonar.sonarValues)
        self.setSpeed(lin_vel, ang_vel, abs((s-0.5)/lin_vel), sonar)
        # aggiornare la nuova posizione del robot

    
    def detect_person(self, sonar):
        for i in range(len(sonar.sonarValues)):
            if sonar.sonarValues[i] <= 0.75:
                if i==0:
                    print("Person detected with sonar SonarFront")
                else:
                    print("Person detected with sonar SonarBack")
                return True
        return False

    def selectMinDistance(self, distances):
        min_distance = float("inf")
        index = 0

        for i in range(len(distances)):
            if distances[i] < min_distance:
                min_distance = distances[i]
                index = i

        return min_distance, index


        