def linear_search(arr:list[int], num:int) -> None:
    n = len(arr)
    for i in range(0,n):
        if arr[i]==num:
            return i
    return -1

if __name__=="__main__":

    arr = [12, 1, 9, 6, 4, 32]
    num = 6
    result = linear_search(arr, num)

    if result == -1:
        print("Element is not present in the array.")
    else:
        print("Element is present at index :",result)