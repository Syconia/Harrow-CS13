

# Set up Node Class
class Node:
    # Init with null as default next and Data as inputted
    def __init__(self, DATA):
        self.__Data = DATA
        self.__Next = None

    # Return the stored data
    def getData(self):
        return self.__Data

    # Return the stored next node
    def getNext(self):
        return self.__Next

    # Change the data inside
    def setData(self, DATA):
        self.__Data = DATA

    # Change the next node
    def setNext(self, NEXT):
        self.__Next = NEXT


# Init the linked list class
class LinkedList:
    # No parameters and default header to null
    def __init__(self):
        self.header = None

    # Check if header is null and return true if it is and false if not
    def isEmpty(self):
        if self.header is None:
            return True
        else:
            return False

    # Add a node to the list
    def addNode(self, nodeData):
        # Init new node
        NODE = Node(nodeData)
        # if the header is null, then set the new node as head
        if self.header is None:
            self.header = NODE
        # else, set it as head and set the next node to previous node
        else:
            NODE.setNext(self.header)
            self.header = NODE

    # Remove the front by temporarily storing the node and setting head to next in line. Delete the node afterwards
    def removeFront(self):
        if self.isEmpty():
            raise IndexError
        temp = self.header
        self.header = temp.getNext()
        del temp

    # Removing the last node in line, or first in
    def removeLast(self):
        if self.isEmpty():
            raise IndexError
        # store the current position basically
        temp = self.header
        counter = 0
        # until the temp is not null
        while temp is not None:
            # iterate through the nodes
            temp = temp.getNext()
            counter += 1
        # delete the node selected
        del temp

        # if the list is now empty, then make the header null
        if self.header.getNext() is None:
            self.header = None
        # otherwise
        else:
            # have a current position again
            temp = self.header
            # iterate through to the last node
            for i in range(counter - 2):
                temp = temp.getNext()

            # if there is nothing, then the list is empty
            if temp is None:
                self.header = None
            else:
                # otherwise make the node point to null
                temp.setNext(None)

    # Iterate through the list with a counter and return the counter
    def size(self):
        temp = self.header
        counter = 0
        while temp is not None:
            counter += 1
            temp = temp.getNext()
        return counter

    # Iterate through the list and return true if there is a node with the same inputted data
    def search(self, DATA):
        temp = self.header
        while temp is not None:
            if temp.getData() == DATA:
                return True
            else:
                temp = temp.getNext()
        # Else return false
        return False

    # Convenience
    def __str__(self):
        temp = self.header
        returnString = ""
        while temp is not None:
            returnString += str(temp) + " "
            temp = temp.getNext()
        return returnString

    def stringValues(self):
        temp = self.header
        returnString = ""
        while temp is not None:
            returnString += str(temp.getData()) + " "
            temp = temp.getNext()
        return returnString


# Ordered Linked List class inheriting from LinkedList class
class OrderedLinkedList(LinkedList):
    # Inits
    def __init__(self):
        super().__init__()

    # Override addNode method to make sure things are in order
    def addNode(self, nodeData):
        NODE = Node(nodeData)
        # Check to see if need to make first node
        if self.header is None:
            self.header = NODE
        # If not, then iterate through the list to find the position with a counter
        else:
            temp = self.header
            counter = 0
            # Try to find the fist node that is bigger than the added node
            while temp.getData() <= NODE.getData():
                temp = temp.getNext()
                counter += 1
                # conditional end, just in case
                if temp is None:
                    break

            # make the bigger node a temp var
            nextNode = temp

            # It helps for some reason
            if counter == 1:
                self.header.setNext(NODE)
                if self.size() >= 2:
                    NODE.setNext(nextNode)
            elif counter == 0:
                self.header = NODE
                NODE.setNext(nextNode)
            # Loop through using counter to find the last node smaller than the added node
            else:
                temp = self.header
                for i in range(counter - 1):
                    temp = temp.getNext()
                # set the last smallest node to link to the added node
                temp.setNext(NODE)
                # if it is not the last node, then set the added node to link to the biggest node
                if counter - 1 < self.size():
                    NODE.setNext(nextNode)
