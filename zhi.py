class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
def InitList(L,listnum):#正向建立链表
    L.val=listnum[0]
    tail=L
    for i in range(1,len(listnum)):
        tail.next=Node(0)
        tail=tail.next
        tail.val=listnum[i]
        tail.next=None
    return L
def Reverse(L):#递归方式反转链表
    if L.next==None or L==None:
        return L
    else:
        newhead=Reverse(L.next)
        L.next.next=L
        L.next=None
        return newhead
def Reversesec(L):#非递归方式反转链表
    if L==None or L.next==None:
        return L
    head=L
    pre=L
    cur=L.next
    temp=L.next.next
    while cur:
        temp=cur.next
        cur.next=pre
        pre=cur
        cur=temp
    head.next=None
    return pre
L=InitList(Node(0),[1,2,3,4])
L=Reversesec(L)
while L:
    print(L.val)
    L=L.next
while L:
    print(L.val)
    L=L.next



