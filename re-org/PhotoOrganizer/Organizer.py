import os
from PIL import Image
from PIL.ExifTags import TAGS

class Organizer:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def getMetaData(self,location):
        print("Getting metadata from images")
        image = Image.open(location)
        exifdata = image.getexif()
        for tagid in exifdata:
             tagname = TAGS.get(tagid, tagid)
             value = exifdata.get(tagid)
             print("{tagname:25}: {value}")

    def createFolder(self):
        print("Created folder")

    def start(self):
        source_loc = input("Enter source location:")
        for root, dirs, files in os.walk(source_loc):
            for single_file in files:
                if ".jpg" in single_file:
                    parent_dir = root
                    full_path = os.path.join(parent_dir,single_file)
                    print(" \n jpg file is present:", full_path )
                    getMetaData("Hi")

