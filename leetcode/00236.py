# https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=daily-question&envId=2024-01-29

class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack = []


    def push(self, x: int) -> None:
        self._send_items_from_one_stack_to_another(self.queue, self.stack)
        self.stack.append(x)
        self._send_items_from_one_stack_to_another(self.stack, self.queue)


    def pop(self) -> int:
        return self.queue.pop()


    def peek(self) -> int:
        return self.queue[-1]

    def _send_items_from_one_stack_to_another(self, origin_stack, target_stack):
        while len(origin_stack) != 0:
            target_stack.append(origin_stack.pop())

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
