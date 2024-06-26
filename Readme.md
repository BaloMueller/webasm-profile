# Webassembly Profile Page for Sebastian Müller

Used CV of Version 2024.2 to generate a Streamlit website for Sebastian Müller as a Profile Homepage.

## Installation

### Conda environment

### To create a conda environment
```bash
conda create -n webasm "python>=3.11" 

# or to update
conda update -n webasm "python>=3.11"

# To activate the environment
conda activate webasm
```

### To install dependencies
```bash
# local installation of the package:
pip install .

# editable install:
pip install -e .
```

### To run the app in Development Mode

```bash
streamlit run src/app.py
```