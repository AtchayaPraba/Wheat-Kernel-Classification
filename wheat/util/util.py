import yaml
from wheat.exception import WheatException
import sys


def read_yaml_file(file_path:str) -> dict:
    """
    Reads a .yaml file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise WheatException(e,sys) from e

