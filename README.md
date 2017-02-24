##Map_Nearby_Places

Map Nearby Places is RESTful service written in Python/Flask to help you find and rate interesting places near you.

[![Build Status](https://travis-ci.org/gkeswani92/Map_Nearby_Places.svg?branch=master)](https://travis-ci.org/gkeswani92/Map_Nearby_Places)

## Manual Installation

###Clone the repository: 
``` 
git clone https://github.com/gkeswani92/Map_Nearby_Places.git 
```

###Install requirements.txt: 
``` 
sudo apt-get pip
pip install requirements.txt 
```

###Run the server: 
```
python setup.py 
```

## Docker
```
docker run -ti -p 8000:8000 map_nearby_places python setup.py
```
