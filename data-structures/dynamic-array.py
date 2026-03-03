class DynamicArray():
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        print("creating array")
        return ([None] * capacity)
        
    def __resize(self, capacity):
        temp = self.__create_array(capacity)
        for i in range(self.capacity):
            temp[i] = self.A[i]
        self.A = temp
        self.capacity = capacity
        print("reized")

    def __str__(self):
        elements = []
        for i in range(self.n):
            elements.append(str(self.A[i]))
        return "[" + ", ".join(elements) + "]"
        
    def append(self, item):
        if self.capacity == self.n:
            self.__resize(self.capacity * 2)
        self.A[self.n] = item
        self.n += 1
        print(f"added {item}")

    def pop(self, index=None):
        if self.n == 0:
            raise IndexError("pop from empty array")
        if index is not None and (index < 0 or index >= self.n):
            raise IndexError("index out of range")
        if index is None:
            index = self.n - 1
        
        value = self.A[index]
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i+1]
        
        self.A[self.n - 1] = None
        self.n -= 1

        return value
            
    def clear(self):
        self.n = 0
        self.capacity = 1
        self.A = self.__create_array(self.capacity)
        print("array cleared")

    
if __name__ == '__main__':
    array = DynamicArray()
    array.append(2)
    print(array)
    array.append(9)
    print(array)
    print(array.pop())
    print(array)
    array.append(9)
    array.append(4)
    array.append(3)
    print(array)
    print(array.pop(2))
    print(array)
    array.clear()
    print(array)