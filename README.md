# Skull-Stripping-CNN-Classifier
Data Mining Term Project.

## Repo Overview: 

This repo contains the sourcecode for team 3's semester long Skull Stripping Classifier project. 
Each file is outlined below:

### Processing Scripts
- This directory contains two files **parse.py** and **to_csv.py**, these files both are used to parse and then extract labels from the additional 125 nifti files added from the NFBS skull-stripped-databased. Details on how to use them are in the comments of each file

### model1.ipynb
- This file contains the training script & necessary data preprocessing for **Model 1** outlined in the presentation and project report.

### model2.ipynb/torch_preProcessing.ipynb
- This file contains the training script & necessary data preprocessing for **Model 2** outlined in the presentation and project report.

### data_exploration.ipynb
- This file contains some preliminary data exploration & code to create some of the graphs used in the report.

### preprocessing.ipynb
- This file contains the data preprocessing used isolated into one notebook and was used in the initial phases of the project before moving data preprocessing to each individual model file for simplicity. 

---

## BSE_BET_DATA Instructions 
Use the following code in the kernel to download and unzip the data files.
```
import requests <br>
import zipfile

url = "https://dyslexia.computing.clemson.edu/BET_BSE/BSE_BET_DATA.zip"
response = requests.get(url, verify=False)

with open("BSE_BET_DATA.zip", "wb") as f:<br>
  f.write(response.content)

zip_file_path = 'BSE_BET_DATA.zip'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:<br>
  zip_ref.extractall('image_data')
```

### Link for additional dataset:
[http://preprocessed-connectomes-project.org/NFB_skullstripped/]

Download the NFBS skull-stripped images file (about 2 gigs)
