# DS-4002-Project-3
## Section 1: Software and Platform 
For this project we used python and specific packages listed below. The platforms used were Windows and Mac and the types of software being used were Juypter notebook and the kernels: Python 3.9 (pytorch).  
### Required imports and libraries:
```python
from torchvision import datasets, transforms
from collections import Counter
import os
from torchvision import datasets, transforms
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torchvision import models
from sklearn.metrics import classification_report
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
```

## Section 2: Map of Documentation 

## Section 3: Instructions for Reproducing
## reminder to edit the folder names once the hierarchy is built 

### 3.0 Assumptions
- You are starting from the repository root (the same folder that contains `README.md`).
- Python ≥ 3.9 is installed.
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
   cd path/to/this/repository
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
python SCRIPTS/01_preprocess.py
```



