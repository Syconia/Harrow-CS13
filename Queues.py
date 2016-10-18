
# Queue Class
class Queue():
    # Init with Contents in a list and Length as an int
    def __init__(self, INTLength):
        # Have a static max size
        self.maxSize = INTLength
        # Variable length
        self.amount = 0
        # Lists for storage
        self.values = []
        self.buffer = []
        # And pointer init
        self.pointer = 0

    # Dequeue
    def enqueue(self, other):
        # Put everything in the buffer first
        self.buffer.append(other)
        # If the list length is less than max size, then append the thing in
        if len(self.values) < self.maxSize:
            self.values.append(self.buffer[0])
            # Remove used variables from buffer
            del self.buffer[0]
            # Increment size
            self.amount += 1
        else:
            # If the list is too long, raise an exception
            if self.amount > self.maxSize:
                raise IndexError
            else:
                # Else leave it in the buffer and increment amount
                self.amount += 1

    # Dequeue
    def dequeue(self):
        # Check where the pointer is
        if self.pointer < self.maxSize:
            # Move pointer up and decrease size
            self.pointer += 1
            self.amount -= 1
            # Return the pointed value
            return self.values[self.pointer - 1]
        else:
            # If there is something in the buffer and pointer is at max
            if len(self.buffer) != 0:
                # Append that in the buffer
                self.values.append(self.buffer[0])
                # Remove buffer value and the first item in the queue
                del self.buffer[0]
                del self.values[0]
                # Decrease amount
                self.amount -= 1
                # Return the newly added value
                return self.values[self.pointer - 1]
            else:
                # If buffer is empty, raise an exception
                raise IndexError
