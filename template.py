import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO)

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

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating enpty file:{filepath}")
    else:
        logging.info(f"{filename} already exists!")