import time

class Sonar:
    def __init__(self, memory_service, sensor= "SonarFront", value= 1.0, duration = 3.0):
        self.memory_service = memory_service
        self.sensor = sensor
        self.duration = duration
        self.value = value
        self.sonarValueList = ['Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value',
                               'Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value' ]

        
    def set_sonar(self):
        mkey = self.sonarValueList[0]
        self.memory_service.insertData(mkey,self.value)
        mkey = self.sonarValueList[1]
        self.memory_service.insertData(mkey,self.value+0.5)
        time.sleep(self.duration)
        self.sonarValues =  self.memory_service.getListData(self.sonarValueList)
        