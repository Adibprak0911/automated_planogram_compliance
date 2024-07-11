import urllib.request

# URLs of the required files
urls = {
    'yolov3.weights': 'https://pjreddie.com/media/files/yolov3.weights',
    'yolov3.cfg': 'https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg',
    'coco.names': 'https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names'
}

# Download each file
for filename, url in urls.items():
    print(f"Downloading {filename} from {url}...")
    urllib.request.urlretrieve(url, filename)
    print(f"{filename} downloaded.")