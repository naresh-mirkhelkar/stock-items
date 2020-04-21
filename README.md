# stock-items
This project helps in identify items in a given pictures and drawing a block around it. 
Uses OpenCV libraries and caffemodel files for object identification.

## Setting Application runtime environment

Application uses gunicorn as its webserver and use the below syntax to execute it....

Ensure pythong path is set right so gunicorn finds all the relevant modules...

```export PYTHONPATH='<path to controller folder>'```

```gunicorn --bind 0.0.0.0:5000 StockResource:app```



