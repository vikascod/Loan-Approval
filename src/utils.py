import os
import sys
import pickle
from src.exception import CustomException

def save_object(file_path, object):
    """
    Save a Python object to a file using pickle.

    Parameters:
        file_path (str): The path to the file where the object will be saved.
        object: The Python object to be saved.

    Raises:
        CustomException: If an error occurs while saving the object.

    Example:
        save_object('model.pkl', trained_model)
    """
    try:
        # Ensure the directory path exists or create it.
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Serialize and save the object to the specified file.
        with open(file_path, 'wb') as file_obj:
            pickle.dump(object, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
