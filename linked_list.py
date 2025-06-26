class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def insertb(self,data):
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            
    def inserti(self,data,index):
        if index==0:
                self.insertb(data)
                return
        position=0
        current_node=self.head
        while current_node is not None and position+1 !=index:
                position+=1
                current_node=current_node.next
        if current_node is not None:
                new_node=Node(data)
                new_node.next=current_node.next
                current_node.next=new_node
        else:
                print("index is not range")        
    def Printll(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next
                   
        
                
                
l1=LinkedList()
l1.insertb(10)
l1.insertb(20)  
l1.insertb(30)
l1.inserti(40, 1) 
l1.Printll()

                
            