#!"C:\Python310\python.exe"
from random import randint


def permute_with_all(arr=list):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[randint(1, n)]
