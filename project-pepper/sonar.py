import time
import math

class Sonar:
    def __init__(self, memory_service, sensor= "SonarFront", duration = 3.0):
        self.memory_service = memory_service
        self.sensor = sensor
        self.duration = duration
        self.sonarValueList = ['Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value',
                               'Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value' ]
        self.robot_position = (0,0) #deve diventare paremetrico

        
    def set_sonar(self):

        distances = self.get_distances(self.robot_position)

        mkey = self.sonarValueList[0]
        self.memory_service.insertData(mkey,distances)
        mkey = self.sonarValueList[1]
        self.memory_service.insertData(mkey,None) #disabled
        time.sleep(self.duration)
        self.sonarValues =  self.memory_service.getListData(self.sonarValueList)
        print(self.sonarValues)


    #we use only the frontal sonar, so it will discover only humans in front of him
    def get_positions(self):
        human1_position = (1,0)
        human2_position = (2,0)
        humans_positions = [human1_position, human2_position]

        return humans_positions

    def get_distances(self, robot_position):
        distances = []

        humans_positions = self.get_positions()
        for pos in humans_positions:
            distance = math.sqrt((robot_position[0]-pos[0])**2 + (robot_position[1]-pos[1])**2)
            distances.append(distance)

        return distances
        