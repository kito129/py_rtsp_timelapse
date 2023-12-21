import os
from datetime import datetime

def rename_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            old_path = os.path.join(root, file_name)

            # Extract the file extension
            base_name, ext = os.path.splitext(file_name)

            # Parse the original timestamp from the filename
            original_timestamp = base_name.split('-')[0]
            original_date = datetime.strptime(original_timestamp, '%d%m%y')

            # Format the new timestamp in the desired format
            new_timestamp = original_date.strftime('%y%m%d')

            # Construct the new file name
            new_name = f"{new_timestamp}-{base_name.split('-')[1]}{ext}"

            new_path = os.path.join(root, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {file_name} to {new_name}')

# Specify the folder path
folder_path = ['./DATA/back',
                './DATA/entrance',
                './DATA/gardenSouth',
                './DATA/garden'
                ]
# Call the function to rename files in the specified folder and its subfolder
for folder_path in folder_path:
    rename_files(folder_path)