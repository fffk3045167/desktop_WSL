def shellSort(arr):

    n = len(arr)
    gap = int(n/2)
    
    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i

            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = int(gap/2)
    return arr

def show(arr):
    print("排序后的数组: ")
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print('\nend')

# 测试数组
arr = [64, 34, 25, 12, 22, 11, 90]

show(shellSort(arr))
