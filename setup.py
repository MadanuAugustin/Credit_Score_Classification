
from setuptools import setup, find_packages
from typing import List


HYPEN_DOT_E = '-e .'

def getrequirements(file_path:str)->List[str]:
    required = []
    with open(file_path) as file_obj:
        required = file_obj.readlines()
        required = [req.replace("\n", '') for req in required]

        if HYPEN_DOT_E in required:
            required.remove(HYPEN_DOT_E)

    return required


setup(
    name='credit_score_classification',
    version='0.0.01',
    author='Augustin',
    author_email='augustin7766@gmail.com',
    install_requires = getrequirements('requirements.txt'),
    packages = find_packages(),   ## find_packages searches for the folders which are having __init__ constructor and converts them to packages
)
