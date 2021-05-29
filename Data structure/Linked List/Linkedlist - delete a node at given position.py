






#Linkedlist


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

    def deleteNode(self, position):
        counter = 0
        temp = self.head

        #If head node is the key node
        if position == 0:
            print("Element present as head node")
            self.head = temp.next
            return           

        #Traverse to find the key data node
        while(counter < position):
            previousNode = temp
            temp = temp.next
            counter += 1

        
        if temp == None:
            print("Element not present in the list")
        elif temp.next == None:
            print("Element present as last node")
            previousNode.next = None
            temp = None
        else:
            print("Element present inside the list")
            previousNode.next = temp.next
            temp = None


llist = LinkedList()
llist.pushData(10)
llist.pushData(20)
llist.pushData(30)
llist.pushData(40)
llist.pushData(50)



llist.deleteNode(4)

llist.printLinkedList()


