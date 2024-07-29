import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
from datetime import datetime
from tqdm import tqdm
import time

def get_image_creation_date(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None
        for tag, value in exif_data.items():
            if TAGS.get(tag) == 'DateTimeOriginal':
                return value
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
        return None

def organize_images_by_date(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        print(' The count of files in {0} is {1}'.format(root, len(files)))
        for file in tqdm(files, desc="Copying inner files"):
            if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
                file_path = os.path.join(root, file)
                creation_date = get_image_creation_date(file_path)

                if creation_date:
                    date_obj = datetime.strptime(creation_date, "%Y:%m:%d %H:%M:%S")
                    date_folder = date_obj.strftime('%Y-%B-%d')
                    new_folder_path = os.path.join(destination_folder, date_folder)

                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)

                    shutil.move(file_path, os.path.join(new_folder_path, file))
                else:
                    print(f"No creation date found for {file_path}")
            else :
                if file.lower().endswith(".mp4"):
                    file_path = os.path.join(root, file)
                    new_folder_path = os.path.join(destination_folder, 'videos')
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)
                    shutil.move(file_path, new_folder_path)
                    #doing nothing as of now
                    print('')


if __name__ == "__main__":
    source_folder = "/Volumes/SSD_Subbu/Toshiba_HDD/Entire_Data_Backup/POP_OS_BackUp/Photos"
    destination_folder = "/Volumes/Photos_HDD/Media_Phots_Videos"
    organize_images_by_date(source_folder, destination_folder)