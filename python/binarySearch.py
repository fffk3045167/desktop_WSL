 # 二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
 # 返回x在arr中的索引，如果不存在返回-1
def binarySearch(arr, l, arrlen, x):
    
    if arrlen >= l:
        mid = int(l + (arrlen - l) / 2)

        # 元素正好在中间位置
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        
        else:
            return binarySearch(arr, mid+1, arrlen, x)
    
    else:
        return -1

def show(index):

    if index == -1:
        print("元素不在数组中")
    
    else:
        print("元素在数组中的索引为: {}".format(index))

 # 测试数组
arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
x = 10

 # 调用函数
show(binarySearch(arr, 0, len(arr)-1, x))

