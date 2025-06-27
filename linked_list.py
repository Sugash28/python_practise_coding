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

class Solution:
       def addtwonumbers(self,l1,l2): 
               L1=""
               L2=""
               while l1.head is not None:
                       L1+=str(l1.head.data)
                       l1.head=l1.head.next
               print(L1)
                       
               while l2.head is not None:
                       L2+=str(l2.head.data)
                       l2.head=l2.head.next
               print(L2)
               o=int(L1)+int(L2)
               print(o)
               out=[]
               for i in str(o):
                        out.append(int(i))
               print(out)
                       
        

                   
        
                
                
l1=LinkedList()
l2=LinkedList()
l1.insertb(2)
l1.insertb(4)  
l1.insertb(3)
l2.insertb(5)
l2.insertb(6)  
l2.insertb(4)
s=Solution()
s.addtwonumbers(l1,l2)




                
            