#二分法
#例：利用二分法查找一个有序列表中是否存在某个数 如查看数字8是否在[1,3,5,7,9]中
def Dichotomy(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]<target:
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
        else:
            return True
    return False