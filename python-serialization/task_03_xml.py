#!/usr/bin/env python3
"""Serialization and Deserialization with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The output XML file name
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file back into a Python dictionary.

    Args:
        filename (str): The input XML file name

    Returns:
        dict: The deserialized dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return None
