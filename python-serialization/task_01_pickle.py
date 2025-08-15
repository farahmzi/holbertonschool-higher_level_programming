#!/usr/bin/env python3
"""Pickling Custom Classes"""

import pickle


class CustomObject:
    """Custom class with serialization and deserialization support"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to the specified file using pickle.
        Returns True if successful, otherwise False.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.
        Returns an instance of CustomObject or None on error.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
