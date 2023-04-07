# Skull-Stripping-CNN-Classifier
Data Mining Term Project.


# Use the following code in the kernel to download and unzip the data files.

import requests \n
import zipfile

url = "https://dyslexia.computing.clemson.edu/BET_BSE/BSE_BET_DATA.zip"
response = requests.get(url, verify=False)

with open("BSE_BET_DATA.zip", "wb") as f:
  f.write(response.content)

zip_file_path = 'BSE_BET_DATA.zip'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
  zip_ref.extractall('image_data')
