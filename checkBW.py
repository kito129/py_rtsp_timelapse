from PIL import Image
import numpy as np
import os

def is_bw(img_path):
    with Image.open(img_path) as img:
        img = img.convert('RGB')
        # Convert image to numpy array
        img_array = np.array(img)
        # Calculate the variance across color channels
        variance = np.var(img_array[:,:,0] - img_array[:,:,1]) + np.var(img_array[:,:,1] - img_array[:,:,2])
        return variance < 20  # Threshold for determining if it's black and white

def check_images_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.jpg'):  # Check only JPG files
            full_path = os.path.join(directory_path, filename)
            if is_bw(full_path):
                print(f"{filename}: Black and White")
            else:
                print(f"{filename}: Color")



# Example usage
directory_path = 'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/back\MAIN'
check_images_in_directory(directory_path)
