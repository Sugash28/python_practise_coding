# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the value of the node
        self.next = None  # Initialize the next pointer to None (no next node yet)

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None (empty list)

    # Method to append a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        
        # If the linked list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the last node and append the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    # Method to print the linked list
    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to delete a node by value
    def delete_node(self, key):
        current = self.head
        
        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # Search for the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # If the node was not found
        if current is None:
            print("Node not found.")
            return
        
        # Unlink the node from the list
        prev.next = current.next
        current = None

# Example usage of the LinkedList class
if __name__ == "__main__":
    llist = LinkedList()
    
    # Append nodes to the list
    llist.append(10)
    llist.append(20)
    llist.append(30)
    
    # Insert node at the beginning
    llist.insert_at_beginning(5)
    
    # Print the linked list
    print("Initial Linked List:")
    llist.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> None
    
    # Delete a node
    llist.delete_node(20)
    
    print("Linked List after deleting 20:")
    llist.print_list()  # Output: 5 -> 10 -> 30 -> None
