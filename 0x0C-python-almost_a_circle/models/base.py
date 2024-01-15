#!/usr/bin/python3
"""

Module creates a class Base

"""
import json
import csv


class Base:
    """
    Meta class for all the classes in this project
    This class manages the 'id' attribute in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates objects of class Base
        id (int and optional): defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string of list dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return (f"[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs"""
        if list_objs is None or len(list_objs) == 0:
            return None
        file_to_write = cls.__name__ + ".json"
        list_items = [i.to_dictionary() for i in list_objs]
        with open(file_to_write, 'w') as f:
            data = cls.to_json_string(list_items)
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        if json_string is None:
            return (f"[]")
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance attributes set"""
        if cls.__name__ == 'Square':
            dummy = cls(1)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                list_dicts = cls.from_json_string(f.read())
                list_instances = [cls.create(**i) for i in list_dicts]
                return list_instances
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serealises in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialises from CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_f, fieldnames=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
