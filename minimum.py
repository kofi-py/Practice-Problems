#!"C:\Python310\python.exe"

def minimum(arr=list):
    """
    Given a list. Returns the minimum value in the list.
    """
    m = arr[1]
    for i in range(2, len(arr)):
        if m > arr[i]:
            m = arr[i]
    return m

arr = [5, 4, 7, 9, 3, 6, 2, 1, 8]
print(minimum(arr))