#!"C:\Python310\python.exe"
from random import randint

def randomize_in_place(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[randint(i, n)]

