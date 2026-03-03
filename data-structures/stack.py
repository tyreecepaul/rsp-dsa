class SpecialStack():
    def __init__(self):
        self.stack = []
        self.minEle = float('inf')
    
    def __str__(self):
        return str(self.stack)

    def push(self, item):
        if not self.stack:
            self.minEle = item
            self.stack.append(item)

        elif item < self.minEle:
            self.stack.append(2 * item - self.minEle)
            self.minEle = item
        else:
            self.stack.append(item)

    def pop(self):
        if not self.stack():
            return 
        
        top = self.stack.pop()
        
        if top < self.minEle:
            self.minEle = 2 * self.minEle - top

    def peek(self):
        if not self.stack():
            return -1
        
        top = self.stack[-1]

        return self.minEle if self.minEle > top else top

    def getMin(self):
        if not self.stack:
            return -1
        return self.minEle
    
    
if __name__ == "__main__":
    stack = SpecialStack()
    stack.append(2)
    stack.append(4)
    stack.append(3)
    stack.append(1)
    stack.append(6)
    print(stack)
    stack.pop()
