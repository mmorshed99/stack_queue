#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#push(x) – Push element x onto stack.
#pop() – Removes the element on top of the stack.
#top() – Get the top element.
#getMin() – Retrieve the minimum element in the stack.
#Note that all the operations have to be constant time operations.
#Q: What should getMin() do on empty stack? 
#A: In this case, return -1.
#
#Q: What should pop do on empty stack? 
#A: In this case, nothing. 
#
#Q: What should top() do on empty stack?
#A: In this case, return -1
#
class MinStack:
    # @param x, an integer
    def __init__(self):
       self.stack = []
       self.minstack = []
    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[len(self.minstack)-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[len(self.minstack)-1])
        


    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            del self.stack[len(self.stack)-1]
            del self.minstack[len(self.minstack)-1]


    # @return an integer
    def top(self):
        if len(self.stack) > 0:
          return self.stack[len(self.stack)-1]
        return -1


    # @return an integer
    def getMin(self):
        if len(self.minstack) > 0:
            return self.minstack[len(self.minstack)-1]
        return -1
