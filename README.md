##Live Review Places

Live Review Places is RESTful service written in Python/Flask to help you find and rate interesting places near you using the Google Places API and the Yelp Fusion API.

[![Build Status](https://travis-ci.org/gkeswani92/Live_Review_Places.svg?branch=master)](https://travis-ci.org/gkeswani92/Live_Review_Places) [![Coverage Status](https://coveralls.io/repos/github/gkeswani92/Map_Nearby_Places/badge.svg)](https://coveralls.io/github/gkeswani92/Map_Nearby_Places)

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
python run.py
```

## Docker
```
docker build -t map_nearby_places .

#Deprecated after switching to VOLUME from ADD: 
docker run -ti -p 8000:8000 map_nearby_places python run.py

docker run -ti -p 8000:8000 -v `pwd`:/code map_nearby_places python run.py
```
