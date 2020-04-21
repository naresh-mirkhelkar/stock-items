import sys
sys.path.append('model')
sys.path.append('controller')

from flask import Flask, request, Response
# import argparse
import controller.StockServices as ss
import cv2
import jsonpickle
import numpy as np


app = Flask(__name__)

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
#
# ap.add_argument("-p", "--prototxt", default='controller/MobileNetSSD_deploy.prototxt.txt', help="path to Caffe 'deploy' prototxt file")
# ap.add_argument("-m", "--model", default='controller/MobileNetSSD_deploy.caffemodel', help="path to Caffe pre-trained model")
# ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
# args = vars(ap.parse_args())
# net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

args = {
    'prototxt' : 'MobileNetSSD_deploy.prototxt.txt',
    'model' : 'MobileNetSSD_deploy.caffemodel',
    'confidence': 0.5
}

net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])


@app.route('/api/healthcheck')
def healthcheck():
    return 'Yes, service is healthy!'


@app.route('/api/processimage', methods=['POST'])
def processimage():
    print("-----Begin Image processing-----")
    # convert string of image data to uint8
    nparr = np.frombuffer(request.data, np.uint8)
    fileName = request.args.get('filename')
    supObj = ss.objectDetection(nparr, net, args, fileName)
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(supObj)
    print("-----End Image processing-----")
    return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run()

