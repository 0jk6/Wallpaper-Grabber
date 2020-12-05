import os
import requests, ctypes
from sys import platform
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
    
    #set wallpaper on windows
    def setNewWallpaperWin(self):
        print("* Setting desktop wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.export_name , 0)
        print("* Wallpaper set successfully")

    #set wallpaper on linux, tested it on Gnome desktop
    def setNewWallpaperGnome(self):
    	print("* Setting desktop wallpaper")
    	cmd = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + os.path.abspath(self.export_name)
    	os.system(cmd)

def main():
    #defining img object    
    img=GetImage(export_name,url)
    img.grabNewImage()

    if platform == 'linux':
    	img.setNewWallpaperGnome()

    if platform == 'win32':
    	img.setNewWallpaperWin()

#running the main() script
if __name__ == "__main__":
    main()
