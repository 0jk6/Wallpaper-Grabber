import requests, ctypes
from datetime import datetime

now = datetime.now()
export_name = now.strftime("%d%m%Y%H%M%S")
export_name=export_name +".jpeg"

url = "https://source.unsplash.com/random/1366x768"

class GetImage():

    def __init__(self,export_name,url):
        self.export_name=export_name
        self.url=url
    def grabNewImage(self):
        print("")
        print("* Fetching wallpaper from the Unsplash")
        try:
            r = requests.get(self.url)
            with open(self.export_name, 'wb') as image:
                image.write(r.content)
            print("* Image saved successfully")
        except:
            print("* Something went wrong")

    def setNewWallpaper(self):
        print("* Setting desktop wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.export_name , 0)
        print("* Wallpaper set successfully")

def main():
    img=GetImage(export_name,url)
    img.grabNewImage()
    img.setNewWallpaper()

if __name__=="__main__":
    main()
