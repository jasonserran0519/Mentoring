class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        # Added a size function to the Queue to help with counting size  
        self.size = 0

    
    def enqueue(self, data):
        node = Node(data)  
        
        # If the Queue is Empty
        if self.isEmpty(): 
            self.head = node
            self.tail = node  
        else:
           # Queue is not Empty, Places node at the end of the List 
           node.prev = self.tail
           self.tail.next = node
           self.tail = node
            
        self.size += 1
        

    def dequeue(self):
        # If Queue is Empty 
        if self.isEmpty():
             return " There is nothing to Dequeue"
        
        remove = self.head 
        
        #If the queue is size 1 
        if self.size == 1:
            self.head = None
            self.tail = None   
        else:
            # Sets A remove pointer on head and shifts all pointers to the right by one
            self.head = self.head.next
            self.head.prev = None
        
        # Decrease size count by 1 for the queue
        self.size -= 1 
        return remove.data


    def peek(self):
        # if queue is empty
        if self.isEmpty():
            return "There is nothing on Queue"
        # Returns head of the list
        return self.head.data


    def Q_size(self):
        #returns size of the queue
        return self.size
        
      


    def isEmpty(self):
        # returns if there is nothing in the Queue (Size is 0)
        return self.size == 0
        
     

    def clear(self):
        #removes everything in remove
        
        # while the size is not 0, the loop will dequeue all nodes until the is is 0
        while not self.isEmpty():
            self.dequeue()
        



    def printQueue(self):
        # prints through all nodes in the list 
        node = self.head
        while node is not None:
            print (node.data, end = " ")
            node = node.next
      

def main():
    myQueue = Queue()
    myarr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in myarr:
        myQueue.enqueue(i)
    

    print(myQueue.peek())
    print(myQueue.dequeue())
    print(myQueue.Q_size())
    print(myQueue.isEmpty())
    


    if not myQueue.isEmpty():
        myQueue.clear()
    myQueue.printQueue()



if __name__ == "__main__":
    main()