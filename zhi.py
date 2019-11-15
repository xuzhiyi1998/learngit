class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
def InitList(L,listnum):
    L.val=listnum[0]
    tail=L
    for i in range(1,len(listnum)):
        tail.next=Node(0)
        tail=tail.next
        tail.val=listnum[i]
        tail.next=None
    return L
def Reverse(L):
    if L.next==None or L==None:
        return L
    else:
        newhead=Reverse(L.next)
        L.next.next=L
        L.next=None
        return newhead
L=InitList(Node(0),[1,2,3,4])
L=Reverse(L)
while L:
    print(L.val)
    L=L.next



