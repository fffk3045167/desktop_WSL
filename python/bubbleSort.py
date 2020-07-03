def bubbleSort(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr)-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def show(arr):
    print("排序后的数组: ")
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print('\nend')

# 测试数组
A = [64, 34, 25, 12, 22, 11, 90]

show(bubbleSort(A))
