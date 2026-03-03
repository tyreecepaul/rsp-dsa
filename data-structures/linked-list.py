class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None 

    def __str__(self):
        return str(self.data)
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, item):
        p = Node(item)
        
        if self.head is None:
            self.head = self.tail = p
        else:
            p.next = self.head
            self.head.prev = p
            self.head = p

    def search(self, item):
        curr = self.head
        while curr:
            if curr.data == item:
                return curr
            curr = curr.next
        return None

    def delete(self, item):
        node = self.search(item)
        if node:
            self.delete_node(node)

    def delete_node(self, node):
        if node is None:
            return

        # Only element
        if node == self.head and node == self.tail:
            self.head = self.tail = None

        # Head
        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        # Tail
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        # Middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def insert_tail(self, item):
        p = Node(item)

        if self.tail is None:
            self.head = self.tail = p
        else:
            p.prev = self.tail
            self.tail.next = p
            self.tail = p
    
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    res = ll.search(3)
    print(res)