class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0  
        
        
    def push (self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1
    
    def pop (self):
        if self.isEmpty():
            return "Stack is Empty"
        remove = self.top
        self.top = self.top.next
        self.size -= 1
        return remove.value
        
    def peek (self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.top.value
    
    def isEmpty(self):
        return self.size == 0

    
    def StK_size(self):
        print (self.size)
    
    def printStack(self): 
        node = self.top
        while node is not None:
            print (node.value, end = " ")
            node = node.next
            
        
        
        

def main():
    mystack = Stack()
    myarr = [1,2,3,4,5,6,7,8,9,10]
    for i in myarr:
        mystack.push(i)

    mystack.peek()
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()

    print(mystack.isEmpty())
    print(mystack.StK_size())

    mystack.push(11)
    mystack.printStack()
    mystack.peek()

    
if __name__ == "__main__":
    main()