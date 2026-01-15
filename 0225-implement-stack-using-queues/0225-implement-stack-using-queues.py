from collections import deque
class MyStack:

    def __init__(self):
       self.item=deque()
    def push(self, x: int) -> None:
        self.item.append(x)
        for _ in range(len(self.item)-1):
            self.item.append(self.item.popleft())

    def pop(self) -> int:
        if len(self.item)==0:
            return -1
        x=self.item.popleft()
        return x

    def top(self) -> int:
        if len(self.item)==0:
            return -1
        return self.item[0]
        

    def empty(self) -> bool:
        return len(self.item)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()