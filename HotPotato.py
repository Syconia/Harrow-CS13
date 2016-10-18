import random, time
from Queues import *

# Queue setup
def setupQueue():
    # Info gathering
    print("Please type in the number of contestants")
    size = input("> ")
    newQueue = Queue(int(size))
    for i in range(int(size)):
        print("Please type in the name of the contestant")
        newName = input("> ")
        newQueue.enqueue(newName)
    return newQueue

# Round function
def hotPotatoRound(QUEUE, FLOATpotatoProbability):
    # It returns so I'm too lazy to have a condition for it
    while True:
        # Store the dequeued value and show who has the potato
        temp = QUEUE.dequeue()
        print(temp + " has the potato")
        # Stick it back at the end of the queue
        QUEUE.enqueue(temp)
        # print(QUEUE.values)

        # Sleep is important. Else it goes too quick
        time.sleep(1)

        # Use random number that is less than 1 to check if they die
        if random.random() > FLOATpotatoProbability:
            # Tell the name of the dead guy
            print("\nHOT POTATO")
            out = QUEUE.dequeue()
            print(out + " is out!\n")

            # Init a new queue
            returnQueue = Queue(QUEUE.amount)
            # print(QUEUE.values)
            # Add values to the queue
            for i in range(QUEUE.amount):
                returnQueue.enqueue(QUEUE.dequeue())
            # print(returnQueue.values)
            # Return queue
            return returnQueue

# mainloop
def mainLoop():
    # Flavour text
    print("WELCOME TO THE HOT POTATO 5000\n")
    print("SETUP\n")
    # Set up the main queue
    mainQueue = setupQueue()
    print("\nGAME START\n")
    # THERE CAN ONLY BE ONE!!!
    while len(mainQueue.values) != 1:
        mainQueue = hotPotatoRound(mainQueue, 0.75)
    # Flavour text
    print(mainQueue.dequeue() + " is the winner!")

mainLoop()
