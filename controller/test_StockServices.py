import sys
sys.path.append('controller')
sys.path.append('model')

import unittest
import cv2
import StockServices as ss
import numpy as np

class Test_StockServices(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.args = {
            'prototxt': 'MobileNetSSD_deploy.prototxt.txt',
            'model': 'MobileNetSSD_deploy.caffemodel',
            'confidence': 0.5
        }

        cls.net = cv2.dnn.readNetFromCaffe(cls.args['prototxt'], cls.args['model'])

    def test_imageclassfiication(self):
        filename = 'diff-sizes-object.jpeg'
        img = cv2.imread('test-images/' + filename)
        _, img_encoded = cv2.imencode('.jpg', img)
        data = img_encoded.tostring()
        # convert string of image data to uint8
        nparr = np.frombuffer(data, np.uint8)
        response = ss.objectDetection(nparr, self.net, self.args, filename)
        print(response)
        self.assertIsNotNone(response)

    def test_noObjectimageclassfiication(self):
        filename = 'no-object.jpeg'
        img = cv2.imread('test-images/' + filename)
        _, img_encoded = cv2.imencode('.jpg', img)
        data = img_encoded.tostring()
        # convert string of image data to uint8
        nparr = np.frombuffer(data, np.uint8)
        response = ss.objectDetection(nparr, self.net, self.args, filename)
        print(response)
        self.assertTrue(response.getImageDetails().isShelfEmpty)


if __name__ == '__main__':
    unittest.main()

