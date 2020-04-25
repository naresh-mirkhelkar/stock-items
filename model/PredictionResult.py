import sys
sys.path.append('../model')
sys.path.append('./controller')


class PredictionResult:

    def __init__(self, imageName, isEmptyShelf):
        self.imageName = imageName
        self.isShelfEmpty = isEmptyShelf


    def getImageDetails(self):
        return self

    def setShelfEmptyStatus(self, status):
        self.isShelfEmpty = status


