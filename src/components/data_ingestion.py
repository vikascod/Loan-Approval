import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion, specifying default paths for training, testing, and raw data files.

    Attributes:
        train_data_path (str): path for the training data file.
        test_data_path (str): path for the testing data file.
        raw_data_path (str): path for the raw data file.

    Example:
    config = DataIngestionConfig()
    train_path = config.train_data_path
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "loan.csv")


class DataIngestion:
    """
    Class responsible for data ingestion tasks.

    This class initializes an instance with a default data ingestion configuration.

    Attributes:
        ingestion_config (DataIngestionConfig): An instance of the DataIngestionConfig class
            containing paths for data files.

    Example:
    data_ingestion = DataIngestion()
    config = data_ingestion.ingestion_config
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # Log a message indicating the entry into the data ingestion method or component.
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset from a CSV file into a Pandas DataFrame.
            df = pd.read_csv(os.path.join("data/loan_approval.csv"))
            logging.info("Read the dataset as a DataFrame")

            # Create directories for data storage if they don't exist.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the entire dataset as raw data.
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split the dataset into training and testing sets.
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training and testing sets as separate CSV files.
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            # Log a message indicating the completion of data ingestion.
            logging.info("Ingestion of the data is completed")

            # Return the paths to the training and testing data.
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
