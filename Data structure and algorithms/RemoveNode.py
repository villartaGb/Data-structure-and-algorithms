
class Node:
    def _init_(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        
        # If the linked list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Otherwise, traverse to the end of the list and append the new node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, index):
        # If the linked list is empty
        if self.head is None:
            print("The list is empty.")
            return
        
        # Store the head node
        temp = self.head

        # If the head needs to be removed
        if index == 0:
            self.head = temp.next
            temp = None
            return

        # Find the node before the node to be removed
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        # If the index is out of range
        if temp is None or temp.next is None:
            print("Index out of range.")
            return

        # Remove the node
        next = temp.next.next
        temp.next = None
        temp.next = next

    def print_list(self):
        # Traverse the linked list and print each node's data
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


my_list = LinkedList()


my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

# Print the list after appending
print("List after appending elements:")
my_list.print_list()

# Remove the element at index 3 (which is '4')
my_list.remove(3)

# Print the list after removing the element
print("List after removing element at index 3:")
my_list.print_list()