# Queue class (FIFO: First In First Out)
class Queue:
    def __init__(self):
        self.queue = []   # List to store queue elements

    # Add element to the end of queue (enqueue)
    def enqueue(self, data):
        self.queue.append(data)   # Insert at end

    # Remove element from front of queue (dequeue)
    def dequeue(self):
        if len(self.queue) == 0:  # Check if queue is empty
            print("Queue is empty")
            return None
        return self.queue.pop(0)  # Remove first element

    # Show the front element
    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None
        return self.queue[0]      # Return first element

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        print("Queue:", self.queue)


# Example usage
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()           # Output: [10, 20, 30]

print("Removed:", q.dequeue())  # Removes 10

print("Front element:", q.peek())

q.display()