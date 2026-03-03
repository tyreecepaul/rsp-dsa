class Node():
    # Singly Linked-List
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"
    
    def enqueue(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1 

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.size -= 1 
        return temp

    def isEmpty(self):
        return self.head is None
    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.front.data
    
    def size(self):
        return self.size
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
