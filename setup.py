from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace('\n', "") for requirement in requirements]
    
    return requirements


setup(
    name="loan_approval",
    version='0.0.1',
    author='Vikas',
    author_email='vikas1618072@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)