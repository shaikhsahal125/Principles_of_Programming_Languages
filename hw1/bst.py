class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    temp = Node(None)
    if root is None:
        temp.data = data
        temp.left = None
        temp.right = None
        root = temp
        return
    else:
        pNode = root
        if pNode.data is data:
            return
        else:
            while pNode is not None:
                if data > pNode.data:
                    if pNode.right is None:
                        temp.data = data
                        temp.left = None
                        temp.right = None
                        pNode.right = temp
                        return
                    else:
                        pNode = pNode.right
                elif data < pNode.data:
                    if pNode.left is None:
                        temp.data = data
                        temp.left = None
                        temp.right = None
                        pNode.left = temp
                        return
                    else:
                        pNode = pNode.left
                else:
                    if pNode.data is data:
                        return


def query(root, data, list):
    flag = 1
    pNode = root
    while pNode is not None:
        if pNode.data is data:
            if flag == 1:
                print("found: root")
                return
            else:
                print("found: ", end="")
                for i in list:
                    print(i, end="")
                print()
                return
        elif data < pNode.data:
            flag = 0
            pNode = pNode.left
            list.append("l ")
        elif data > pNode.data:
            flag = 0
            pNode = pNode.right
            list.append("r ")

    print("not found")
    return


c, i = input().split()
if c == "i":
    root = Node(int(i))
else:
    print("not found")

list = []

try:
    while True:
        c2, i2 = input().split()
        if c2 == "i":
            insert(root, int(i2))
        elif c2 == "q":
            list = []
            query(root, int(i2), list)
except Exception:
    pass
