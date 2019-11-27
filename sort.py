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
listnum=[2,5,7,1,9,3]
print(InsertSort(listnum))
