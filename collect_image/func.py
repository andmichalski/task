import requests

def download_image(url):
    data = requests.get(url).content
    with open("image.jpg", "wb") as handler:
        handler.write(data)