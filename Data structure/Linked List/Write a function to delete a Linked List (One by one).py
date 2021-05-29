


# Write a function to delete a Linked List

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def printLinkedList(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next
    
    def pushData(self, newData):
        newNode = Node(newData)

        temp = self.head
        #Check if head node is empty
        if self.head == None:
            self.head = newNode
            return

        #Else, traverse till the last node of the list
        while(temp.next != None):
            temp = temp.next

        temp.next = newNode

    def deleteNode(self):

        temp = self.head
        while(temp):
            nextNode = temp.next
            del temp.data
            temp = nextNode


llist = LinkedList()
llist.pushData(10)
llist.pushData(20)
llist.pushData(30)
llist.pushData(40)
llist.pushData(50)



llist.deleteNode()

# llist.printLinkedList()


