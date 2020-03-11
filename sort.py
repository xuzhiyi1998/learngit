"""基础版冒泡排序"""
def BubbSort(listnum):
    for i in range(1,len(listnum)):
        for j in range(0,len(listnum)-i):
            if listnum[j]>=listnum[j+1]:
                listnum[j],listnum[j+1]=listnum[j+1],listnum[j]
    return listnum
"""改进版冒泡排序,增加了一个标志判断是否有交换，没有交换则完成排序"""
def ImproveBubbSort(listnum):
    for i in range(1,len(listnum)):
        flag=0
        for j in range(0,len(listnum)-i):
            if listnum[j]>listnum[j+1]:
                listnum[j],listnum[j+1]=listnum[j+1],listnum[j]
                flag=1
        if not flag:
            break
    return listnum
"""插入排序"""
def InsertSort(listnum):
    for i in range(1,len(listnum)):
        j=i-1
        temp=listnum[i]
        while listnum[j]>temp and j>=0:
            listnum[j+1]=listnum[j]
            j-=1
        listnum[j+1]=temp
    return listnum
"""快速排序"""
def QuickSort(listnum):
    if len(listnum)>=2:
        mid=listnum[len(listnum)//2]
        listnum.remove(mid)
        left,right=[],[]
        for num in listnum:
            if num<mid:
                left.append(num)
            else:
                right.append(num)
        return QuickSort(left)+[mid]+QuickSort(right)
    else:
        return listnum
print(QuickSort([10,11,9,22,3,5,12]))

"""归并排序"""
def MergeSort(lists):
    if len(lists)<=1:
        return lists
    num=len(lists)//2
    left=MergeSort(lists[:num])
    right=MergeSort(lists[num:])
    return Merge(left,right)
def Merge(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]
    result+=right[r:]
    return result

