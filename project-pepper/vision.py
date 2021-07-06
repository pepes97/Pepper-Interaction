from numpy.random import choice


class Vision:
    def __init__(self):
        pass

    
    def cnnForEmotionRecognition(self, image):
        classes = ["Neutral", "Happy", "Sad", "Surprise"]

        prediction = self.forward(image)

        return classes[prediction]


    def forward(self, image):
        list_of_candidates = [0, 1, 2, 3]

        if image == "happyImage":
            weights = [0.1, 0.5, 0.05, 0.35]
        elif image == "neutralImage":
            weights = [0.7, 0.1, 0.1, 0.1]  
        elif image == "sadImage":
            weights = [0.1, 0.05, 0.8, 0.05]  
        elif image == "surpriseImage":
            weights = [0.1, 0.35, 0.05, 0.5]  
        
        output = choice(list_of_candidates, 1, p=weights)[0]

        return output


