
class Gesture:
    def __init__(self, ALMotion):
        self.ALMotion = ALMotion


    def doHello(self):
        jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw", "RHand", "HipRoll", "HeadPitch"]
        angles = [-0.141, -0.46, 0.892, -0.8, 0.98, -0.07, -0.07]
        times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
        isAbsolute = True
        self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        for i in range(2):
            jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
            angles = [1.7, -0.07, -0.07]
            times  = [0.8, 0.8, 0.8]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
            angles = [1.3, -0.07, -0.07]
            times  = [0.8, 0.8, 0.8]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)


        return
    
    def doNo(self):
        for i in range(2):
            jointNames = ["HeadYaw"]
            angles = [0.25]
            times  = [1.0]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["HeadYaw"]
            angles = [-0.25]
            times  = [1.0]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        return


    def doYes(self):
        for i in range(2):
            jointNames = ["HeadPitch"]
            angles = [-0.3]
            times  = [1.0]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["HeadPitch"]
            angles = [0.1]
            times  = [1.0]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        return

    def doRock(self):
        jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "HeadPitch"]

        angles = [1.10, 0.52, -1.36, -1.48, 
                 -1.41, 0.27, 1.29, -0.07,
                 0.68, 0.70, -0.26, 0.31,
                 -0.15, -0.17, 0.28]

        times = [1.0, 1.0, 1.0, 1.0, 
                 1.0, 1.0, 1.0, 1.0, 
                 1.0, 1.0, 1.0, 1.0,
                 1.0, 1.0, 1.0]
        
        isAbsolute = True
        self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        for i in range(5):
            
            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "HeadPitch"]

            angles = [1.10, 0.52, -1.36, -1.48, 
                    -1.41, 0.27, 1.29, -0.07,
                    0.68, 1.48, -0.26, 0.60,
                    0.15, -0.17, -0.43]
                    
            times = [0.5, 0.5,0.5, 0.5, 
                    0.5, 0.5, 0.5, 0.5, 
                    0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5]
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)
            
            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "HeadPitch"]

            angles = [1.10, 0.52, -1.36, -1.48, 
                    -1.41, 0.27, 1.29, -0.07,
                    0.68, 0.70, -0.26, 0.70,
                    -0.15, -0.17, 0.43]
            
            times = [0.5, 0.5,0.5, 0.5, 
                    0.5, 0.5, 0.5, 0.5, 
                    0.5, 0.5, 0.5, 0.5,
                    0.5, 0.5, 0.5]

            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)
        
        return

    def doJazz(self):
        jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

        angles = [1.20, 0.008, -0.65, -1.20, 
                 -0.05, 0.30, 0.33, -0.19,
                 0.40, 1.36, 0.99, 0.60,
                 -0.22, -0.26, -0.14, 0.05]

        times = [1.0, 1.0, 1.0, 1.0, 
                 1.0, 1.0, 1.0, 1.0, 
                 1.0, 1.0, 1.0, 1.0,
                 1.0, 1.0, 1.0, 1.0 ]
        
        isAbsolute = True
        self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)
        
        for i in range(5):
            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [1.20, 0.008, -0.65, -1.20, 
                    -0.05, 0.30, 0.33, -0.19,
                    0.40, 1.36, 0.99, 0.60,
                    0.22, 0.26, 0.05, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
        
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [1.20, 0.008, -0.65, -1.20, 
                    -0.05, 0.30, 0.33, -0.19,
                    0.40, 1.36, 0.99, 0.60,
                    -0.12, -0.26, -0.14, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)
    
    def doClassical(self):
        
        jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

        angles = [0.85, 0.92, -2.07, -0.85, 
                -1.29, 0.43, -0.05, -0.01,
                -0.38, 0.71, 0.99, 0.60,
                0.2, -0.26, -0.14, 0.05]

        times = [1.0, 1.0, 1.0, 1.0, 
                1.0, 1.0, 1.0, 1.0, 
                1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0 ]
              
        
        isAbsolute = True
        self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        for i in range(5):
            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [0.85, 0.92, -2.07, -0.85, 
                    -1.29, 0.43, -0.05, -0.01,
                    0, 0.71, 0.99, 0.60,
                    0.2, -0.26, -0.14, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
                
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [0.85, 0.92, -2.07, -0.85, 
                    -1.29, 0.43, -0.05, -0.01,
                    -0.38, 0.71, 0.99, 0.60,
                    0.2, -0.26, -0.14, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
                
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)
    
    def doPop(self):
        jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

        angles = [1.18, 0.38, 2.07, -0.01, 
                -1.81, 0.43, 0.90, -0.11,
                -0.17, 0.68, 0.38, 0.46,
                0.2, -0.03, -0.01, 0.05]

        times = [1.0, 1.0, 1.0, 1.0, 
                1.0, 1.0, 1.0, 1.0, 
                1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0 ]
              
        
        isAbsolute = True
        self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        for i in range(5):
            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [-1.18, -0.38, -2.07, 0.01, 
                    1.81, -0.43, -0.90, 0.11,
                    0.17, 0.68, -0.38, 0.46,
                    0.0, 0.03, 0.01, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
                
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [1.25, 0.008, -0.12, 0.78, 
                    0.10, 0.02, 0.95, 0.52,
                    -1.85, 0.45, 1.81, 0.46,
                    -0.2, 0.03, 0.01, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
                
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw","LElbowRoll", 
                      "LWristYaw", "LHand", "RShoulderPitch", "RShoulderRoll", 
                      "RElbowYaw","RElbowRoll", "RWristYaw", "RHand", 
                      "HipRoll", "HipPitch", "KneePitch", "HeadPitch"]

            angles = [1.18, 0.38, 2.07, -0.01, 
                    -1.81, 0.43, 0.90, -0.11,
                    -0.17, 0.68, 0.38, 0.46,
                    0.2, -0.03, -0.01, 0.05]

            times = [1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0, 
                    1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 1.0 ]
                
            
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)