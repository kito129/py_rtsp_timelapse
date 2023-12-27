import os
import shutil


source_folder_path = ['D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/back',
                      'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/entrance',
                      'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/gardenSouth',
                      'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/garden'
                      ]


def move_files_to_main_folder(source_folder, destination_folder):
    count = 0
    errorCount = 0
    for root, directory, files in os.walk(source_folder):
        if os.path.basename(root) == 'MAIN':
            for file in files:
                time = int(file[7:13])
                # if this "231226-172907-862746.jpg" the second - is betwen 080000 and 190000
                if time >= 70000 and time <= 190000 and file.endswith('.jpg'):
                    try:
                        subfolder_path = os.path.join(root, file)
                        destination_path = os.path.join(destination_folder, file)
                        shutil.copy(subfolder_path, destination_path)
                        count += 1
                        print (f'Copy: {file} to {destination_folder}')
                    except:
                        print(f'Error with {file}')
                        errorCount += 1
                    
        #for direct in directory:
        #    if direct != 'MAIN':
        #        shutil.rmtree(os.path.join(root, direct))
        #        print(f'Removed: {direct}')
    
    print(f'Total files copied: {count}, in {source_folder.split("/")[-1]}, errors: {errorCount}')


# Replace 'destination_folder_name' with the desired name of the main folder
destination_folder_name = 'DAY'
for source_folder_path in source_folder_path:
    # Create the main folder path
    destination_folder_path = os.path.join(source_folder_path, destination_folder_name)

    # Create the main folder if it doesn't exist
    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)

    # Move files to the main folder
    move_files_to_main_folder(source_folder_path, destination_folder_path)