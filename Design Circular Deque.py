class MyCircularDeque:

    k = 0
    deque = []
    def __init__(self, k: int):
        self.k = k
        self.deque = []
        

    def insertFront(self, value: int) -> bool:
        if(len(self.deque) == self.k):
            return False
        else:
            self.deque[:0] = [value]
        return True

    def insertLast(self, value: int) -> bool:
        if(len(self.deque) == self.k):
            return False
        else:
            self.deque.append(value)            
        return True
    def deleteFront(self) -> bool:
        if(len(self.deque) == 0):
            return False
        else:
            self.deque.pop(0)
            return True
    def deleteLast(self) -> bool:
        if(len(self.deque) == 0):
            return False
        else:
            self.deque.pop(-1)
            return True

    def getFront(self) -> int:
        if(len(self.deque)>0):
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if(len(self.deque) > 0):
            return self.deque[-1]
        return -1
    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
