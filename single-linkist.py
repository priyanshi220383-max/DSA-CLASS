# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store the value
        self.next = None      # Pointer to the next node (initially None)


# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None      # First node of the list (initially empty)

    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head # Point new node to current head
        self.head = new_node      # Make new node the head

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)     # Create a new node

        if self.head is None:     # If list is empty
            self.head = new_node
            return

        temp = self.head
        while temp.next:          # Traverse till last node
            temp = temp.next

        temp.next = new_node      # Link last node to new node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next  # Move head to next node
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:          # Value not found
            print("Value not found")
            return

        prev.next = temp.next     # Remove node from list

    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Linked List:")
ll.display()

ll.delete(20)

print("After deleting 20:")
ll.display()