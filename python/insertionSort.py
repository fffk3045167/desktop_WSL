# 插入排序
def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            arr[j] = key
            j = j - 1
    return arr

def showArr(arr):
    
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print('\n')

# 测试数组
arr = [12, 11, 34, 13, 1, 5, 25, 19, 6]
showArr(insertionSort(arr))
