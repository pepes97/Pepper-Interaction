
import time

class Motion:
    def __init__(self, motion_service):
        self.motion_service = motion_service


    def setSpeed(self, lin_vel, ang_vel, dtime, sonar):
        self.motion_service.move(lin_vel, 0, ang_vel)
        time.sleep(dtime)
        for _ in range(3):
            for i in range(len(sonar.sonarValues)):
                sonar.sonarValues[i]-=0.1
        self.motion_service.stopMove()
        return sonar

    def forward(self, sonar ,r=3, lin_vel=0.2, ang_vel=0):
        print("Sonar Values", sonar.sonarValues)
        print('Forward ',r)
        detected_p = self.detect_person(sonar)
        if detected_p:
            return True
        s = 0.5*r
        sonar = self.setSpeed(lin_vel, ang_vel, abs(s/lin_vel), sonar)
        detected_p = self.detect_person(sonar)
        if detected_p:
            return True
        else:
            return False
    
    def detect_person(self, sonar):
        for i in range(len(sonar.sonarValues)):
            if sonar.sonarValues[i] <= 0.75:
                if i==0:
                    print("Person detected with sonar SonarFront")
                else:
                    print("Person detected with sonar SonarBack")
                return True
        return False