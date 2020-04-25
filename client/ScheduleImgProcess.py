import requests
import json
import cv2
import datetime
import schedule

def captureImages():

    cv2.namedWindow("preview")
    cam_handle = cv2.VideoCapture(0)

    # create a default image name
    imgname = "testfilenamewithdate"

    addr = 'http://192.168.86.37:5000'
    test_url = addr + '/api/processimage?filename='

    if cam_handle.isOpened():
        rval, frame = cam_handle.read()
    else:
        print("Video camera is not attached!")
        raise Exception('Camera not attached or OpenCV not able to work with camera!')
        return

    try:
        loop = 10
        while rval:
            while loop > 0:
                cv2.imshow("preview", frame)
                rval, frame = cam_handle.read()
                loop = loop -1
            cv2.imshow("preview", frame)
            rval, frame = cam_handle.read()
            # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            imgname = str(datetime.datetime.now().strftime("%x%H%M")).replace("/", "").replace(":", "") + '.jpeg'
            cv2.waitKey(1000)
            cv2.imwrite(imgname,frame)
                # if key == 27: # exit on ESC
            break

        cv2.destroyWindow("preview")
        cam_handle.release()
    except:
        raise Exception('Failed to get frames from OpenCV')

    print("fileName:" + imgname)
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}
    img = cv2.imread(imgname)
    _,img_encoded=cv2.imencode('.jpg', img)
    err, response = requests.post(test_url + imgname, data=img_encoded.tostring(), headers=headers)
    print(json.loads(response.text))
    if err is not None:
        raise err


if __name__ == '__main__':
    schedule.every(10).seconds.do(captureImages)
    while True:
        schedule.run_pending()
