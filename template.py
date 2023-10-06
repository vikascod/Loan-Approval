import os
import logging
from pathlib import Path

# Configure the logging system with the INFO level.
logging.basicConfig(level=logging.INFO)

# Define a list of file paths that need to be created.
list_of_files = [
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/pipelines/__init__.py',
    'src/pipelines/training_pipeline.py',
    'src/pipelines/prediction_pipeline.py',
    'src/exception.py',
    'src/logger.py',
    'src/evaluate.py',
    'src/utils.py',
    'requirements.txt',
    '.gitignore',
    'app.py',
]

# Iterate through the list of file paths.
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object for easier manipulation.
    filedir, filename = os.path.split(filepath) # Split filename and filedir

    # Create directories if they don't exist.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create an empty file if it doesn't exist or is empty.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists!")

