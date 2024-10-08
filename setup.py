### BUILDING APPLICATION AS A PACKAGE

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .' ## this triggers setup.py automatically in requirements.txt, but we dont want to run it again in setup.py

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Jaiwant',
    author_email= 'jaiwantmahun2000@gmail.com',
    packages = find_packages(),
    requires = get_requirements('requirements.txt')
)