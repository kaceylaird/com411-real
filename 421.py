class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0  # Index of the front of the queue
        self.back = -1   # Index of the back of the queue
        self.size = 0    # Current size of the queue

    def add(self, item):
        if self.size < self.capacity:
            self.queue[self.back] = item
            self.back = (self.back + 1) % self.capacity
            self.size += 1
        else:
            print("Queue is full. Cannot add item.")

    def remove(self):
        if self.size > 0:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size = 1
            return item
        else:
            print("Queue is empty. Cannot remove item.")
            return None
    def __str__(self):
        return f"Queue: {self.queue}, Front: {self.front}, Back: {self.back}"

# Example usage:
my_queue = Queue(5)

my_queue.add(1)
my_queue.add(2)
my_queue.add(3)

print(my_queue)  # Output: Queue: [1, 2, 3, None, None], Front: 0, Back: 3

removed_item = my_queue.remove()
print(f"Removed item: {removed_item}")  # Output: Removed item: 1
print(my_queue)  # Output: Queue: [None, 2, 3, None, None], Front: 1, Back: 3
