import sys
sys.path.append('controller')
sys.path.append('model')

import unittest
import StockResource as sr
import cv2


class TestStockResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tester = sr.app.test_client()

    def test_healthcheck(self):
        result = sr.healthcheck()
        self.assertEqual(result, 'Yes, service is healthy!')

    def test_health_using_service(self):
        # tester = sr.app.test_client()
        response = self.tester.get('/api/healthcheck', content_type='html/text')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Yes, service is healthy!')

    def test_object_detection_using_service(self):
        # tester = sr.app.test_client()
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
        filename = 'diff-sizes-bottle.jpeg'
        img = cv2.imread('test-images/' + filename)
        _, img_encoded = cv2.imencode('.jpg', img)
        response = self.tester.post('/api/processimage?filename=' + filename, data=img_encoded.tostring(), headers=headers)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

if __name__ == '__main__':
    unittest.main()


