class Node:
    def __init__(self, node, ref=None):
        self.node = node
        self.ref = None  # Reference to the next node (default is None)
    
class linkedlist:
    def __init__(self):
        self.head = None
    def print(self):
        if self.head is None:
            print("List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.node)
                n=n.ref

ll1=linkedlist(23)
ll2=linkedlist(45)
