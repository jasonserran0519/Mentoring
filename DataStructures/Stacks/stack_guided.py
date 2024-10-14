class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0  

    
    def push(self, value):
        # Is the stack empty?

        # Create a new node, save pointer to current top.

        # Update the top of the stack and set next to previous top.
        pass
    
        if self.isEmpty():
            return "stack is Empty"
        node = Node(value)
        Node.next = self.head.next
        self.head.next = node
        self.size += 1


    def pop(self):
        # Is the stack empty?

        # Delete the node at the top of the stack
        pass


    def peek(self):
        # Is the stack empty?

        # Return the value of the node at the top of the stack
        pass
        if self.isEmpty():
            return "Stack is Empty"
        remove = self.head
        self.head = self.head.next
        self.head.next = remove.next
        self.size -= 1
        delete(remove)


    def isEmpty(self):
        # Is the stack empty?
        pass
        if self.isEmpty():
            return "Stack is Empty"
        return self.head(value)


    def size(self):
        # Is the stack empty?
        pass
        print (self.size)


    def printStack(self):
        # Is the stack empty?
        pass
        node = self.head
        while node.next != NULL:
            print (node(value))
            node = node. next



def main():
    mystack = Stack
    myarr = [1,2,3,4,5,6,7,8,9,10]
    for i in myarr:
        mystack.push(i)

    mystack.peek()
    mystack.pop()
    mystack.printStack()
    mystack.pop()
    mystack.printStack()

    print(mystack.isEmpty())
    print(mystack.size())

    mystack.push(11)
    mystack.printStack()
    mystack.peek()

    
if __name__ == "__main__":
    main()

