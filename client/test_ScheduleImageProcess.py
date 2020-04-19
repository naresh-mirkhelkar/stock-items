import sys
sys.path.append('client')

import unittest
import ScheduleImgProcess as sip

class TestScheduleImageProcess(unittest.TestCase):

    def test_invokeCamera(self):
        with self.assertRaises(Exception):
            sip.captureImages()


if __name__ == '__main__':
    unittest.main()

