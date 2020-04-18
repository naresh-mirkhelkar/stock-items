import requests
import json
import cv2
import datetime
import schedule

def captureImages():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    # create a default image name
    imgname = "testfilenamewithdate"

    addr = 'http://192.168.86.37:5000'
    test_url = addr + '/api/processimage?filename='

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        print("Video camera is not attacched!")
        return
    loop = 10
    while rval:
        while loop > 0:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            loop = loop -1
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        imgname = str(datetime.datetime.now().strftime("%x%H%M")).replace("/", "").replace(":", "") + '.jpeg'
        key = cv2.waitKey(1000)
        cv2.imwrite(imgname,frame)
            # if key == 27: # exit on ESC
        break

    cv2.destroyWindow("preview")
    vc.release()

    print("FILENAME:" + imgname)
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}
    img = cv2.imread(imgname)
    _,img_encoded=cv2.imencode('.jpg', img)
    response = requests.post(test_url + imgname, data=img_encoded.tostring(), headers=headers)
    print(json.loads(response.text))

schedule.every(10).seconds.do(captureImages)
while True:
    schedule.run_pending()
