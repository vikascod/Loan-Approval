from setuptools import find_packages, setup
from typing import List

# Define a function to read requirements from a file and return them as a list.
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace('\n', "") for requirement in requirements]

    return requirements

# Define the setup configuration for the Python package.
setup(
    name="loan_approval",  # Name of the package
    version='0.0.1',  # Version number
    author='Vikas',  # Author's name
    author_email='vikas1618072@gmail.com',  # Author's email address
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=get_requirements('requirements.txt')  # Specify package dependencies from a requirements file
)
