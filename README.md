# stock-items
This project helps in identifying items in a given picture and drawing a block around it. 
Uses OpenCV libraries and caffemodel files for object identification.

The application is divied into client/server archtiectural style. Both the client and server can be run on
same machine but since the intent is to use RaspberryPI, and because its CPU and memory is small, it cannot run the full 
ComputerVision tech stack efficiently. Hence, Client is made to run on raspbeprryPI which integrates with camera and runs as a scheduler

Schedule takes snaps of identified location for every schedule sec/minute and sends this data to server through http connection.

The server collects, the images, runs Deep Neural Network process based on pretrained network of CaffeModel, Identifies the image objects and encloses them in a box.
The object is iddentified based on certain confidence settings. At this stage, a confidence setting of 0.5 is set for object detection.

Before running any tests, below is the prequisite...
1. Install all the requirements byt running the below command...
``` pip3 install -r requirements.txt```

This will install all the required modules on the intended machine. 

### Running test from command line....

```python3 -m unittest controller/test_StockResource.py```

The above test runs all the images from test-images folder, processes and places them in process-images folder.

Open each image to see the identified objects in an enclosed box. 


## Setting Application runtime environment

Application uses gunicorn as its webserver and use the below syntax to execute it....

Ensure python path is set right so gunicorn finds all the relevant modules...

```export PYTHONPATH='<path to controller folder>'```

```gunicorn --bind 0.0.0.0:5000 StockResource:app```

Once the webserver is up and running, find the IP address and port of the server and update it in the client.
Change the scheduler's time based on need. Currently it is set up for 10 secs, which helps in testing.


Run the client using...

``` python3 client/ScheduleImgProcess.py```

### Tech Stack:
1. Python 3.7
2. pip3
3. gunicorn

### Modules:
1. Opencv -- Installed as opencv-contrib-python
2. numpy
3. jsonpickle
4. schedule
5. requests
6. json
7. datetime
8. os
9. unittest
