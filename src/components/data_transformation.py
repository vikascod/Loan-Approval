import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.logger import logging
from src.exception import CustomException
import os
import sys
from dataclasses import dataclass
from src.utils import save_object

label_encoder = LabelEncoder()

@dataclass
class DataTransformationConfig:
    """
    Configuration class for data transformation, specifying the path for saving the preprocessing object.
    """
    preprocessing_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    """
    Class responsible for data transformation tasks, including preprocessing and feature scaling.
    """
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
            categorical_columns = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]

            # Define a numerical data processing pipeline with imputation and standard scaling.
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='median')),
                ('scalar', StandardScaler())
            ])

            # Define a categorical data processing pipeline with imputation and one-hot encoding.
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])

            logging.info(f"Numerical Columns: {numerical_columns}")
            logging.info(f"Categorical Columns: {categorical_columns}")

            # Create a ColumnTransformer for applying the numerical and categorical pipelines.
            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns),
            ])
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Read the training and testing data from CSV files.
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test files")

            # Obtain the data transformation (preprocessing) object.
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "Loan_Status"
            numerical_columns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]
            categorical_columns = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Property_Area"]

            # Divide the datasets into independent and dependent features.
            input_features_train_df = train_df.drop(columns=[target_column_name, 'Loan_ID'], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Fit and transform the target feature for both train and test datasets
            target_feature_train_encoded = label_encoder.fit_transform(target_feature_train_df)
            target_feature_test_encoded = label_encoder.transform(target_feature_test_df)

            logging.info("Applying preprocessing on training and test dataframes")

            # Apply preprocessing to the training and testing dataframes.
            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Combine the preprocessed features with the encoded target feature.
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_encoded)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_encoded)]

            # Save the preprocessing object.
            logging.info("Saved preprocessing object")
            save_object(
                file_path=self.data_transformation_config.preprocessing_obj_file_path,
                object=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessing_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
