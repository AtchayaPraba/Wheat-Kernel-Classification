import os
from setuptools import setup, find_packages
from typing import List

# Declaring variable for get_requirements_list function
REQUIREMENTS_FILE_DIR = "e:\\iNeuron\\ML_internship\\Wheat-Kernel-Classification"
REQUIREMENTS_FILE_NAME = "requirements.txt"
REQUIREMENTS_FILE_PATH = os.path.join(REQUIREMENTS_FILE_DIR, REQUIREMENTS_FILE_NAME)
HYPHEN_E_DOT = "-e ."

# Declaring variable for setup function
PROJECT_NAME = "wheat-kernel-classification"
PROJECT_VERSION = "0.0.1"
PROJECT_AUTHOR = "Atchaya Praba"
PROJECT_DESCRIPTION = """
INTERNSHIP PROJECT 
    Project Title: Wheat Kernel Classification
    Problem Statement: 
        Measurements of geometrical properties of kernels belonging to three different varieties of wheat. 
        A soft X-ray technique and GRAINS package were used to construct all seven, real-valued attributes. 
        The examined group comprised kernels belonging to three different varieties of wheat: Kama, Rosa and Canadian, 70 elements each, randomly selected for the experiment.
        The data set can be used for the tasks of classification and cluster analysis.
    Dataset:
        The test group consisted of kernels from three different wheat varieties: Kama, Rosa, and Canadian, each with 70 components, chosen at random for the experiment. 
        A soft X-ray approach was used to identify high-quality visualization of the interior kernel structure. 
        It is non-destructive and far less expensive than more advanced imaging techniques such as scanning microscopy or laser technology.
        KODAK X-ray plates measuring 13x18 cm were used to capture the images. 
        Combine harvested wheat grain from experimental fields was used in the research, which was carried out at the Institute of Agrophysics of the Polish Academy of Sciences in Lublin.
"""

# Function to get the list of strings form requirements.txt file
def get_requirements_list ()->List[str]:
    """
    Description: Returns the list of requirements or libraries mentioned in the requirements.txt file
    Return type: List[str]
    """
    with open(REQUIREMENTS_FILE_PATH) as file:
        requirement_list = file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    author=PROJECT_AUTHOR,
    description=PROJECT_DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

# python setup.py install