import sys
sys.path.append('controller')
sys.path.append('model')
import jsonpickle
import numpy as np
import cv2
import model.SupervisableImage as si
import model.ImageType as it



# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

IGNORE = set(["background", "aeroplane", "bicycle", "bird", "boat",
	 "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"])
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")


def objectDetection(nparr, net, args, filename):
    # req = request
    # convert string of image data to uint8
    # nparr = np.frombuffer(req.data, np.uint8)

    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    print("length %s, wideth %s", (img.shape[0]), img.shape[1])

    #cv2.imshow("Preview", img)

    (h, w) = img.shape[:2]
    print(" %s,w %s", (h, w))
    blob = cv2.dnn.blobFromImage(img,
                                 0.007843, (300, 300), 127.5)
    # do some fancy processing here....
    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > args["confidence"]:
            # extract the index of the class label from the
            # `detections`
            idx = int(detections[0, 0, i, 1])

            # if the predicted class label is in the set of classes
            # we want to ignore then skip the detection
            if CLASSES[idx] in IGNORE:
                continue

            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the prediction on the frame
            # label = "{}: {:.2f}%".format(CLASSES[idx],
            #                              confidence * 100)
            label = "{}: {:.2f}%".format("SKU:12345",
                                         confidence * 100)
            cv2.rectangle(img, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(img, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


    # fileName = req.args.get("filename")
    print("Query parm for filanem:%s", filename)

    cv2.imwrite('processed-images/' + filename, img)

    # # build a response dict to send back to client
    # response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
    #             }
    # # encode response using jsonpickle
    # response_pickled = jsonpickle.encode(response)
    #
    # print(response_pickled)

    supImage = si.SupervisableImage(filename, 'size={}x{}'.format(img.shape[1], img.shape[0]), it.ImageType.JPEG)

    return supImage