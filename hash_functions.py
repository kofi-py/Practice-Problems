#!"C:\Python310\python.exe"
from math import floor

class HashFunctions(dict):
    def __init__(self, slots=int, key=int):
       self.m = slots
       self.k = key
    def simple_uniform_hashing(self) -> int:
        return floor(self.k * self.m)
    def division_method(self):
        return (self.k) % (self.m)
    def multiplaction_method(self, A):
        return floor(self.m*((self.k*A) % 1))
    
       
       


