
from django.test import TestCase

# Create your tests here.
from datetime import datetime

class Tset(objedt):
    """
    Time sets maintain the states of a set data structure over time.
    """

    def __init__(self, value=None, at=None):
        self._data = dict()
        if value is None:
            return
        self.value = value
        self.at = datetime()

        
        
        
