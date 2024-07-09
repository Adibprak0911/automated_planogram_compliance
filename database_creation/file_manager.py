import os
import shutil

# Define the paths
source_base_path = 'database_creation/frames/lays'
destination_path = 'database_creation/frames/lays_final'

# Ensure the destination folder exists
os.makedirs(destination_path, exist_ok=True)

# Counter for naming files numerically
counter = 1

# Iterate through each folder
for i in range(1, 11):
    folder_path = os.path.join(source_base_path, str(i))
    
    if os.path.exists(folder_path):
        # Iterate through each file in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            if os.path.isfile(file_path):
                # Define new filename
                new_filename = f'{counter}.jpg'
                new_file_path = os.path.join(destination_path, new_filename)
                
                # Copy file to the destination folder
                shutil.copy(file_path, new_file_path)
                
                # Increment counter
                counter += 1

print("Files have been successfully combined and renamed.")
