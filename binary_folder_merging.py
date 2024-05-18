import os
import shutil
import time

start = time.process_time()

# Assign directories
input_directory = 'D:\\Test_code\\'
output_directory = 'C:\\Users\\admin\\OneDrive\\Desktop\\Fresh_Output\\'

def merge_dir(in_directory, out_directory):
    # Define the name of the new folder
    instrument_folder = os.path.join(out_directory, "Instruments")

    # Ensure the instrument folder exists
    if not os.path.exists(instrument_folder):
        os.makedirs(instrument_folder)

    # List all subdirectories in the source directory
    subdirectories = [d for d in os.listdir(in_directory) if os.path.isdir(os.path.join(in_directory, d))]

    for subdir in subdirectories:
        subdir_path = os.path.join(in_directory, subdir)
        # List all items in the subdirectory
        entries = os.listdir(subdir_path)

        # Initialize an empty list to store the names of directories
        inner_folders = []

        # Iterate through each entry in the directory
        for d in entries:
            # Construct the full path of the entry
            full_path = os.path.join(subdir_path, d)

            # Check if this path is a directory
            if os.path.isdir(full_path):
                # If it's a directory, add it to the list
                inner_folders.append(d)

        for inner_folder in inner_folders:
            inner_folder_path = os.path.join(subdir_path, inner_folder)
            dest_inner_folder_path = os.path.join(instrument_folder, inner_folder)

            # Ensure the destination inner folder exists
            if not os.path.exists(dest_inner_folder_path):
                os.makedirs(dest_inner_folder_path)

            # Copy all items from inner folder to the destination inner folder
            for item in os.listdir(inner_folder_path):
                src_item_path = os.path.join(inner_folder_path, item)
                dest_item_path = os.path.join(dest_inner_folder_path, item)

                if os.path.isfile(src_item_path):
                    if not os.path.exists(dest_item_path):
                        shutil.copy2(src_item_path, dest_item_path)
                        print(f"Copied file '{src_item_path}' to '{dest_item_path}'")
                elif os.path.isdir(src_item_path):
                    if not os.path.exists(dest_item_path):
                        shutil.copytree(src_item_path, dest_item_path)
                        print(f"Copied directory '{src_item_path}' to '{dest_item_path}'")
                    else:
                        # Merge directories
                        for sub_item in os.listdir(src_item_path):
                            src_sub_item_path = os.path.join(src_item_path, sub_item)
                            dest_sub_item_path = os.path.join(dest_item_path, sub_item)
                            if not os.path.exists(dest_sub_item_path):
                                shutil.copy2(src_sub_item_path, dest_sub_item_path)
                                print(f"Copied file '{src_sub_item_path}' to '{dest_sub_item_path}'")


merge_dir(input_directory, output_directory)

print("Time taken to execute the code in seconds:", time.process_time() - start)
