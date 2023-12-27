import os
import shutil

def move_files_to_main_folder(source_folder, destination_folder):
    count = 0
    for root, directory, files in os.walk(source_folder):
        if not (os.path.basename(root) == 'MAIN' or os.path.basename(root) == 'DAY'):
            for file in files:
                subfolder_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(subfolder_path, destination_path)
                count += 1
                print (f'Moved: {file} to {destination_folder}')
                
        #for direct in directory:
        #    if direct != 'MAIN':
        #        shutil.rmtree(os.path.join(root, direct))
        #        print(f'Removed: {direct}')
    
    print(f'Total files moved: {count}, in {source_folder.split("/")[-1]}')



source_folder_path = ['D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/back',
                      'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/entrance',
                      'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/gardenSouth',
                      'D:/00_projects/02_homeAutomation/06_py_rtsp_timelapse/DATA/garden'
                      ]

# Replace 'destination_folder_name' with the desired name of the main folder
destination_folder_name = 'MAIN'
for source_folder_path in source_folder_path:
    # Create the main folder path
    destination_folder_path = os.path.join(source_folder_path, destination_folder_name)

    # Create the main folder if it doesn't exist
    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)

    # Move files to the main folder
    move_files_to_main_folder(source_folder_path, destination_folder_path)
