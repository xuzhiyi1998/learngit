class Tree():
    def __init__(self,x=None):
        self.val=x
        self.left=None
        self.right=None
class TreeMethod():#构建二叉树
    def InitTree(self,root):
        value=int(input("请输入一个数字:"))
        if value:
            root.val=value
            root.left=Tree()
            root.right=Tree()
            self.InitTree(root.left)
            self.InitTree(root.right)
        return root
    def HierPrint(self,root):#层次遍历二叉树
        queue=[root]#存储队列
        outlist=[]#输出结果
        while queue:
            current=[]
            numflag=len(queue)
            i=0
            while i<numflag:
                point=queue.pop(0)
                if point.val:
                    current.append(point.val)
                if point.left:
                    queue.append(point.left)
                if point.right:
                    queue.append(point.right)
                i+=1
            if len(current):
                outlist.append(current)
        return outlist
    def visit(self,root):
        if root.val:
            print(root.val)
    def PreOrder(self,root):#先序遍历
        if root:
            self.visit(root)
        if root.left:
            self.PreOrder(root.left)
        if root.right:
            self.PreOrder(root.right)
    def MidOrder(self,root):#中序遍历
        if root.left:
            self.MidOrder(root.left)
        if root:
            self.visit(root)
        if root.right:
            self.MidOrder(root.right)
    def BackOrder(self,root):#后序遍历
        if root.left:
            self.BackOrder(root.left)
        if root.right:
            self.BackOrder(root.right)
        if root:
            self.visit(root)
