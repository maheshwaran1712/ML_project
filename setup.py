from setuptools import find_packages,setup
from typing import List
setup_trigger='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if setup_trigger in requirements:
            requirements.remove(setup_trigger)
    return requirements
setup (
    name='ML_Project',
    version='0.0.1',
    description='First End to End Project',
    author="Mahesh",
    author_email='maheshwaran.er@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)