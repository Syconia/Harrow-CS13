
# Stack class
class Stack():
    # Put in a list and set a limit. If limit is less than 0, it's basically infinitely large
    def __init__(self, List, INTlimit):
        self.Values = List
        if INTlimit < 0:
            INTlimit = 99999
        self.Limit = INTlimit
        # Set up pointer. It's set by list index so start from 0. If empty, it's false
        if self.Values == []:
            self.Pointer = False
        else:
            self.Pointer = len(List)-1
        # If pointer exists, then check if it's over the limit
        if self.Pointer != False:
            if self.Limit < self.Pointer + 1:
                raise IndexError

    # Add item to top of stack
    def push(self, item):
        # Check to see if it's over the limit
        if self.Pointer + 2 > self.Limit:
            raise IndexError
        # Check to see if it's at top of list
        try:
            # If not, then change next value to item
            self.Values[self.Pointer + 1] = item
        except IndexError:
            # else, add new value
            self.Values.append(item)
        # Pointer update
        if self.Pointer == False:
            self.Pointer = 0
        else:
            self.Pointer += 1

    # Return top item, do not delete
    def pop(self):
        returnValue = self.Values[self.Pointer]
        # Update pointer
        self.Pointer -= 1
        return returnValue

    # Empty the stack, reset the pointer
    def emptyStack(self):
        self.Values = []
        self.Pointer = False

    # For convenient printing
    def __str__(self):
        return str(self.Values)
