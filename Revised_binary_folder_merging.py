import os
import shutil

input_directory = "C:\\Users\\admin\\PycharmProjects\\Test input\\bin - Copy (3) - Copy\\"
output_directory = "C:\\Users\\admin\\PycharmProjects\\Test input\\outbin\\"

def merge_dir(in_directory, out_directory):
    # Define the name of the new folder
    instrument_folder = os.path.join(out_directory, "Instruments")

    # Ensure the instrument folder exists
    if not os.path.exists(instrument_folder):
        os.makedirs(instrument_folder)

    i = 0  # Initialize the folder index
    while True:
        folder_name = str(i)
        folder_path = os.path.join(in_directory, folder_name)
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' not found. Exiting loop.")
            break

        print(f"Processing folder: {folder_path}")

        # List all subdirectories in the current folder and sort them
        subdirectories = sorted([d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))])
        print(f"Subdirectories found: {subdirectories}")

        for subdir in subdirectories:
            subdir_path = os.path.join(folder_path, subdir)
            dest_subdir_folder_path = os.path.join(instrument_folder, subdir)

            print(f"Preparing to move contents from '{subdir_path}' to '{dest_subdir_folder_path}'")

            # Ensure the destination subdir folder exists
            if not os.path.exists(dest_subdir_folder_path):
                os.makedirs(dest_subdir_folder_path)

            # List all items in the subdir folder and sort them
            entries = sorted(os.listdir(subdir_path))

            for item in entries:
                src_item_path = os.path.join(subdir_path, item)
                dest_item_path = os.path.join(dest_subdir_folder_path, item)

                if os.path.isfile(src_item_path):
                    if not os.path.exists(dest_item_path):
                        shutil.move(src_item_path, dest_item_path)
                        print(f"Moved file '{src_item_path}' to '{dest_item_path}'")
                elif os.path.isdir(src_item_path):
                    if not os.path.exists(dest_item_path):
                        shutil.move(src_item_path, dest_item_path)
                        print(f"Moved directory '{src_item_path}' to '{dest_item_path}'")
                    else:
                        # Merge directories
                        for sub_item in os.listdir(src_item_path):
                            src_sub_item_path = os.path.join(src_item_path, sub_item)
                            dest_sub_item_path = os.path.join(dest_item_path, sub_item)
                            if not os.path.exists(dest_sub_item_path):
                                shutil.move(src_sub_item_path, dest_sub_item_path)
                                print(f"Moved file '{src_sub_item_path}' to '{dest_sub_item_path}'")

        i += 1  # Increment the folder index

merge_dir(input_directory, output_directory)
