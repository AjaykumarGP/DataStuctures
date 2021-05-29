




#Linked list

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
        while(temp):
            print(temp.data)
            temp = temp.next

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

    def deleteKeyNode(self, keyData):
        temp = self.head
        if temp.data == keyData:
            self.head = temp.next
            temp = None
            return

        while(temp != None):
            if temp.data == keyData:
                break
            previousNode = temp
            temp = temp.next
        
        if temp == None:
            print("Element not present")
            return
        elif temp.next is None:
            print("Element found and deleted from last node")
            previousNode.next = None
            temp = None
            return
        elif temp.data == keyData:
            print("Element found and deleted from middle node")
            previousNode.next = temp.next
            temp = None    


llist = LinkedList()

llist.head = Node(10)

#Add the node as a last node
llist.pushDataToLast(20)
llist.pushDataToLast(30)
llist.pushDataToLast(40)
llist.pushDataToLast(50)

#Deleting the node from the list using the key data
llist.deleteKeyNode(100)


#Print the linkedlist
llist.printLinkedList()





