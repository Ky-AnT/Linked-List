import os

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

#First node is called the header (linked list must know where the header is, so that we can find what other values are)

class linkedList:
    def __init__(self, header=None):
        self.header = header

    def append(self, newNode):
        #Function appends a node into a linked list (append - to add a node at the end of a list)
        current = self.header
        if current:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            #Appending a node in an empty linked list
            self.header = newNode

    def display(self):
        current = self.header
        if current:
            guiList = []
            while current.next:
                guiList.append(str(current.value))
                current = current.next
            guiList.append(str(current.value))
            return '->'.join(guiList)
    def len(self):
        length = 1
        current = self.header
        if current:
            while current.next:
                current = current.next
                length += 1
        else:
            length = 0
        return length
    def insert(self,node,position):
        #Possible scenarios:
        #len(list) > position
        #len(list) < position or the list is empty
        #↳We will add the node to the end of the list, or as the first value of the list
        if position <= 1:
            node.next = self.header
            self.header = node
        elif self.len() > position:
            current = self.header
            counter = 2
            #Traverses through the list, until we have reached the node after we need to insert the new node
            while counter < position and current.next != None:
                #Sets current node to the following node in the list
                current = current.next
                #Increases counter by one
                counter += 1
            #Sets the 'next' value for the node, to what the current's 'next' value was
            node.next = current.next
            #Sets current's new 'next' value to the node, as we have inserted a new value in the linked list
            current.next = node
        elif position == self.len():
            current = self.header
            counter = 1
            while counter < self.len()-1:
                current = current.next
                counter += 1
            node.next = current.next
            current.next = node
        elif position > self.len():
            self.append(node)
    def delete(self, position):
        if position == 1 and self.len() > 0:
            self.header = self.header.next
        elif position <= self.len():
            current = self.header
            counter = 1
            while counter < self.len()-1:
                current = current.next
                counter += 1
            current.next = None
        else:
            print("You gave a position that is greater than the length of the list!")

def init(length,startInt,increment):
    linkedListArray = linkedList(0)
    for i in range(length):
        linkedListArray.append(Node(startInt+(i)*increment))
    return linkedListArray
    

getLen = int(input("Please provide length of your linked list: "))
getStart = int(input("Now, please provide starting integer: "))
getIncrement = int(input("Finally, please give step between values of list: "))

output = init(getLen,getStart,getIncrement)
print(f"The linked list {output.display()} has been saved to 'output'")

while True:
    userInput = input("""Commands:
(a) Insert
(b) Append
(c) Display
(d) Delete
(q) Quit
Type a command (a-c,q): """)
    if userInput.lower() == 'a':
        val, pos = int(input("Value to insert: ")), int(input("Position to insert: "))
        output.insert(Node(val),pos)
    elif userInput.lower() == 'b':
        val = int(input("Value to append: "))
        output.append(Node(val))
    elif userInput.lower() == 'c':
        print(output.display())
    elif userInput.lower() == 'd':
        print(f'Here is the current list: {output.display()}')
        position = int(input("Position to delete at: "))
        output.delete(position)
    elif userInput.lower() == 'q':
        exit()
