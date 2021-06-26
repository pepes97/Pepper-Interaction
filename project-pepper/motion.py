
import time

class Motion:
    def __init__(self, motion_service):
        self.motion_service = motion_service


    def setSpeed(self, lin_vel, ang_vel, dtime):
        self.motion_service.move(lin_vel, 0, ang_vel)
        time.sleep(dtime)
        self.motion_service.stopMove()

    def forward(self, r=3, lin_vel=0.2, ang_vel=0):
        print('Forward ',r)
        s = 0.5*r
        self.setSpeed(lin_vel, ang_vel, abs(s/lin_vel))