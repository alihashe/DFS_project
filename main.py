from msilib.schema import Class
from typing_extensions import Self
from unicodedata import name
import requests
import pandas as pd


class Node:
    """This defines each location on the map."""
    def __init__(self, name="nihil", location=(-1, -1)):
        self.name = name
        self.location = location

    def returnName(self):
        return self.name

    def returnLocation(self):
        return self.location


  

#39.164737530481396, -86.5129661849151     Forest Dorm