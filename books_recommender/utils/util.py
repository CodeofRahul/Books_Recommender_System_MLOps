# in utility we write common function that is going to using multiple time. we write once in utility and use just by importing it

import yaml
import sys
from books_recommender.exception.exception_handler import AppException



def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e