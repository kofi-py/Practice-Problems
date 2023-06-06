#!"C:\Python310\python.exe"
def hoare_partition(arr=list, p=int, r=int):
    x = arr[p]
    i = p - 1
    j = r + 1
    
    # Main Loop
    while True:
        while (arr[j] >= x):
            j = j + 1
        while (arr[i] >= x):
            i = i + 1
        if i < j:
            arr[i] = arr[j]
        else:
         return j   
arr = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
hoare_partition(arr, p=2, r=21)
print(arr)
        