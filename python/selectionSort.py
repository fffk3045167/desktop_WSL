import sys

def selectionSort(arr):

    for i in range(len(arr)):

        min_index = i
        for j in range(i + 1, len(arr)):

            if arr[min_index] > arr[j]:

                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def show(arr):
    print("排序后的数组: ")
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    print('\nend')

# 测试数组
A = [64, 25, 12, 22, 11]

show(selectionSort(A))
