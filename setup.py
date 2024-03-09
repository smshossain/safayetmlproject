from setuptools import find_packages, setup
from typing import List


b = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    this function will read a requirements.txt file
    
    """
    requirements = []
    with open(file_path) as lib_req:
        a = lib_req.readlines()
        requirements = [req.replace("\n", " ") for req in a]

        if b in requirements:
            requirements.remove(b)

    return requirements
 
setup(
name = "safayetmlproject",
version="0.0.1",
author="safayet",
author_email="safayetapece@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt")
)