import requests, ctypes
from datetime import datetime

#creating names for images with date and time
now = datetime.now()
export_name = now.strftime("%d%m%Y%H%M%S")
export_name=export_name +".jpeg"

#url to scrape images
url = "https://source.unsplash.com/random/1366x768"

#defining the class to get images
class GetImage():
    
    #initializing the needed variables
    def __init__(self,export_name,url):
        self.export_name=export_name
        self.url=url
    
    #this will grab images using requests library and saves it into your computer
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
    
    #this will set new wallpaper and the following code only works on windows
    def setNewWallpaper(self):
        print("* Setting desktop wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.export_name , 0)
        print("* Wallpaper set successfully")

def main():
    #defining img object
    
    img=GetImage(export_name,url)
    img.grabNewImage()
    img.setNewWallpaper()

#running the main() script
if __name__=="__main__":
    main()
