class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Empty Linked List
        self.head = None
        # Number of nodes in the linked list
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        # New node
        new_node = Node(value)
        # Create connection
        new_node.next = self.head
        # Reassign head
        self.head = new_node
        # Increment n
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result += str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def append(self, value):
        # New node to be appended
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the last node
            curr = self.head
            while curr.next != None:
                curr = curr.next
            # Append the new node
            curr.next = new_node
        self.n += 1  # Increment n after successful append

    def insert_after(self, after_value, value):
        """Inserts a new node with the given value after a specific node in the linked list.

        Args:
            after_value: The value of the existing node after which the new node should be inserted.
            value: The value of the new node to be inserted.

        Returns:
            None if successful, or "Item not found" if the target node is not found.
        """ 

        # New node to be inserted
        new_node = Node(value)

        # Traverse the list to find the target node
        curr = self.head
        while curr != None:
            if curr.data == after_value:
                # Found the target node, insert after it
                new_node.next = curr.next
                curr.next = new_node
                self.n += 1
                return  # Insertion successful

            curr = curr.next

        # Target node not found
        return "Item not found"
    def clear(self):
        self.head = None
        self.n = 0
    def delete_head(self):
        """Deletes the first node (head) of the linked list."""

        if self.head == None:
            return "Empty LinkedList"  # Handle empty list case

        self.head = self.head.next  # Update head to point to the next node
        self.n -= 1  
        return "Nothing"
    def pop(self):
        curr = self.head
        if self.head == None:
            return "Empty" 
        if curr.next == None:
            # removed = self.head.data
            self.head = None
            self.n -= 1
            return None
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n-=1
    def remove(self, value):
        curr = self.head
        if self.head == None:
            return "Empty" 
        if curr.data == value:
            self.head = curr.next
            return "Delete value"
        while curr.next != None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.n -= 1
                return "Deleted value"
            curr= curr.next
    def search(self,value):
        curr = self.head
        if self.head == None:
            return -1
        counter = 0
        while curr != None:
            if curr.data == value:
                return counter
            curr = curr.next
            counter += 1
        return 'Not found'
    # def maxelement(self):
    #     curr = self.head
    #     max = curr.data
    #     while curr != None:
    #         if max < curr.next.data:
    #             max = curr.next.data
    #         curr = curr.next
    #     return max 

            

L = LinkedList()
L.append(5)
L.append(4)
print(max(1,10))
print(L.insert_after(50, 3))
L.insert_after(5, 3)
L.insert_after(3, 5)
print(L)
# L.pop()
# print(L.remove(5))
# print(L.remove(5))
# print(L.remove(3))
# print(L.remove(5))
# print(L.remove(5))
print(L.search(3))
# print(L.maxelement())
# L.remove(3)
# L.append(5)

print(L)
# print(len(L))
