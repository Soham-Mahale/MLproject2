from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This fxn will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if  HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name="MLproject2",
version='0.01',
author="Soham Mahale",
package=find_packages(),
install_requries=get_requirements("requirement.txt")

)