def search(arr:list[int],size:int,key:int)-> None:
    if size == 0:
        return -1
    elif arr[size-1]==key:
        return size-1
    return search(arr, size-1, key)

if __name__=="__main__":
    arr = [23, 34, 3, 2, 89]
    size = len(arr)
    key = 3
    result = search(arr, size, key)
    if result == -1:
        print("item not present in array")
    else:
        print("item found at index:",result)