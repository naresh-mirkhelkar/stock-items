import sys
sys.path.append('../model')
sys.path.append('./controller')

import random

class SupervisableImage:

    def __init__(self, imageName, resolution, imgType):
        self.imageName = imageName
        self.imageType = imgType.name
        self.imageId = random.random()
        self.resolution = resolution

    def getImageDetails(self):
        return self

    def getImageId(self):
        return self.imageId
