# DS-4002-Project-3
## Section 1: Software and Platform 
For this project we used python and specific packages listed below.
The platforms used were Windows and Mac and the types of software
being used were Jupyter notebook / Google Colab and the
kernels: Python 3.9 .  
### Required imports and libraries:
``` python
import tensorflow as tf
from google.colab import drive
import os
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dropout, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import json
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
```

## Section 2: Map of Documentation 
```
DS-4002-Project-3/
│
├── README.md                      ← Main orientation + reproduction guide
├── LICENSE.md                     ← MIT License
│
├── DATA/
│   ├── raw/                       ← Raw FruitVision dataset (NOT stored on GitHub)
│   │   └── Original Image/
│   │        └── Fruits Original/
│   │             ├── Apple/
│   │             │    ├── Fresh/
│   │             │    ├── Rotten/
│   │             │    └── Formalin-mixed/       (ignored)
│   │             ├── Banana/
│   │             ├── Grape/
│   │             ├── Mango/
│   │             └── Orange/
│   │
│   ├── dataset_splits/            ← Output of Script 01
│   │   ├── train/
│   │   │    ├── fresh/
│   │   │    └── rotten/
│   │   ├── val/
│   │   │    ├── fresh/
│   │   │    └── rotten/
│   │   └── test/
│   │        ├── fresh/
│   │        └── rotten/
│   │
│   └── metadata_README.md         ← Data dictionary, provenance, ethics, summary, plots
│
├── SCRIPTS/
│   ├── 01_train_val_test_split.py      ← Local script to generate splits from raw data
│   └── 02_train_resnet50_colab.ipynb   ← Colab notebook for training & evaluation
│
├── OUTPUT/
│   ├── best_model.h5                   ← Best Keras model saved during training
│   ├── training_history.json           ← Loss/accuracy per epoch
│   ├── classification_report.json      ← Precision/recall/F1 scores
│   ├── confusion_matrix.png            ← Confusion matrix figure
```
## Section 3: Instructions for Reproducing
### 3.0 Assumptions
- You are starting from the repository root (the same folder that contains `README.md`).
- Python ≥ 3.9 is installed.
- You have access to Google Colab for training the model.
- Commands are shown for macOS/Linux.
  - On Windows PowerShell, replace `source .venv/bin/activate` with:
    - `. .venv/Scripts/Activate.ps1`

**Project-specific assumptions (update these as needed):**
- Raw data files are stored in `DATA/raw/`
- Processed/clean data will be written to `DATA/processed/`
- Model outputs (metrics, figures, and artifacts) will be written to `OUTPUT/`
- All scripts used below are stored in the `SCRIPTS/` directory

---

### 3.1 Set up the Environment
1. Open a terminal and navigate to the project folder (the repo root):

   ```bash
   cd DS-4002-Project-3/
   ```
2. (Recommended) Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
  Windows option: 
  ```bash
  python -m venv .venv
  . .venv/Scripts/Activate.ps1
  ```
3. install all required independencies
``` bash
pip install -r requirements.txt
```
### 3.2 Obtain and Place the Data
1. Download the raw dataset from the source described in Section 2: Map of Documentation
2. Save the raw files into: `DATA/raw/`
3. Verify that the paths in the scripts under `SCRIPTS/` match the actual file names
in `DATA/raw/`. Update them if necessary.

### 3.3 Preprocessing the Raw Data 
From the repo root, run:
``` bash
python SCRIPTS/01_train_val_test_split.py
```
which results to
``` bash
DATA/dataset_splits/train/
DATA/dataset_splits/val/
DATA/dataset_splits/test/
```
Each folder contains
``` bash
Fresh/
Rotten/
```

### 3.4 Upload Dataset Splits to Google Drive
To train on Google Colab, upload the entire folder:
```
DATA/dataset_splits/
```
to
```
My Drive/Colab Notebooks/DS4002-Project3/dataset_splits/
```
Also create (or allow the notebook to create):
```
My Drive/Colab Notebooks/DS4002-Project3/OUTPUT/
```

### 3.5 Train the Model in Google Colab
1. Upload to Google Colab
```
SCRIPTS/02_train_resnet50_colab.ipynb
```
2. Set runtime to GPU:
Runtime → Change runtime type → GPU
3. Run all cells:
4. Mount Google Drive
5. Load dataset from dataset_splits
6. Build ResNet-50 (ImageNet pretrained)
7. Train model with early stopping
8. Evaluate on the test set
9. Save outputs into the Drive OUTPUT/ folder

### 3.6 Move Outputs Back into This Repository
After training completes, download the contents of:
```
My Drive/Colab Notebooks/DS4002-Project3/OUTPUT/
```
and place the files into
```
OUTPUT/
```

You should have
```
OUTPUT/
    best_model.h5
    training_history.json
    classification_report.json
    confusion_matrix.png
```