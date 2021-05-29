




#Linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def pushDataToFront(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def pushDataToMiddle(self, previousNode, newData):
        
        if previousNode is None:
            print("Previous node has to be inside the list")
            return
        newNode = Node(newData)
        newNode.next = previousNode.next
        previousNode.next = newNode

    def pushDataToLast(self, newData):
        newNode = Node(newData)
        #Check if list empty; if so connect newNode with head
        if self.head is None:
            self.head = newNode
        
        #Traverse till the last node of the list
        temp = self.head
        while(temp.next):
            temp = temp.next

        #After getting to the last node, add the newNode to temp.next = newNode
        temp.next = newNode


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

#Start mapping
llist.head.next = second
second.next = third

#Add the node in front of the list
llist.pushDataToFront(0)

#Add the node after the given node
llist.pushDataToMiddle(second, 10)

#Add the node as a last node
llist.pushDataToLast(20)


#Print the linkedlist
llist.printLinkedList()





