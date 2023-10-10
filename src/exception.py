import os
import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    """
    Args:
        error: The error or exception that occurred.
        error_detail: An object that contains information about the error's traceback.

    Returns:
        error_message: A formatted error message containing the file name, line number, and error message.

    Example:
    error_message_detail(exception_object, sys.exc_info())
    """
    # Get the exception traceback information using sys.exc_info().
    exc_type, exc_value, exc_traceback = sys.exc_info()

    # Extract the filename and line number from the traceback.
    filename = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno

    # Create a formatted error message that includes the filename, line number, and the error message itself.
    error_message = f"Error occurred in Python script [{filename}] at line number [{line_number}]: {str(error)}"

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Custom exception class that inherits from the built-in Exception class. It takes an error message
        and error detail as input, and it generates a custom error message based on the provided information.

        Args:
            error_message (str): The main error message or description.
            error_detail: Additional error details, typically obtained using sys.exc_info().

        Example:
        try:
            # Some code that might raise an exception
        except Exception as e:
            # Create a CustomException with a custom error message and error details
            custom_exception = CustomException("An error occurred", sys.exc_info())
            raise custom_exception
        """
        super().__init__(error_message)
        # Generate a custom error message by calling the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Override the __str__ method to provide a string representation of the CustomException.

        Returns:
            str: The custom error message.
        """
        return self.error_message
