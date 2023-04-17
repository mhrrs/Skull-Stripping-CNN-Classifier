import os
import shutil

# I used this script to extract the brain scans from the new data added to the
# project. It scans through src_dir and finds the correct files then adds them
# to the ./out directory

# Use this to generate the out directory, and then run the to_csv script to get
# the correct labels

# I manually copied over the files to wherever your other files are stored 
# and manually pased the additional labels into the raw csv document with the 
# other labels

def move_files():
    # Define the source directory
    src_dir = './NFBS_Dataset'

    # Define the destination directory
    dst_dir = './out'

    # Loop through all files in the source directory and its subdirectories
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Check if the file ends with 'w.nii.gz'
            if file.endswith('w.nii.gz'):
                # Construct the full path of the file
                src_file = os.path.join(root, file)

                # Construct the full path of the destination directory
                dst_file = os.path.join(dst_dir, file)

                # Move the file to the destination directory
                shutil.move(src_file, dst_file)

if __name__ == '__main__':
    move_files()