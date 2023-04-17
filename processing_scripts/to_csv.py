import os
import csv

# This is a function to parse the contents of a folder defined by dir_path
# and output the filenames into a csv followed by a 'No', 'No' classification

# This script was used to add the new perfect scans to the dataset labels

def write_to_csv():
    # Define the directory containing the files
    dir_path = './out'

    # Define the name of the output CSV file
    csv_file = 'labels.csv'

    # Open the output CSV file for writing
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Loop through all files in the directory
        for filename in os.listdir(dir_path):
            # Check if the file is a regular file (i.e., not a directory)
            if os.path.isfile(os.path.join(dir_path, filename)):
                # Write the filename followed by two "No" entries to the CSV file
                writer.writerow([filename, 'No', 'No'])

if __name__ == '__main__':
    write_to_csv()