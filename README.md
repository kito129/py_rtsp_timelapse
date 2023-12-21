# py_rtsp_timelapse
    author: kito129
    date: 2023/12/20
    last update: 2023/12/21
    version: 0.9# author: kito129
    based on project: https://github.com/evgenii-d/rtsp-timelapse

## Description
A command line rstp camera recorder for your timelapse and security camera, written in python, inspired by repo: https://github.com/evgenii-d/rtsp-timelapse 

## Installation
```
git clone 
cd py_rtsp_timelapse
pip install -r requirements.txt
```

## Usage
Configure your camera in config.json
```
{
    "images_folder": "your folder for images",
    "sources": {
      "entrance": {
        "source": "rtsp://user:password@your ip:port/1",
        "interval": "900",
        "quality": "100",
        "color": "YELLOW"
      },
    }
  }
```

Run the script
```
cd rtsp_timelapse
python revisedMain.py
```