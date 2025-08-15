#!/usr/bin/env python3
"""Basic Serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    If the file already exists, it will be replaced.

    Args:
        data (dict): The dictionary to serialize
        filename (str): The output JSON file name
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename (str): The input JSON file name

    Returns:
        dict: The deserialized data
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
