class Node:

    def __init__(self,data):
        self.val = data
        self.nextNode = None

class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        currNode = self.head
        
        if index < 0 or index > self.size :
            return -1
        
        while index:
            #print(currNode.val)
            currNode = currNode.nextNode

            index -= 1

        if not currNode:
            return -1
        return currNode.val


        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.nextNode = self.head
        self.head = newNode 
        self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.size += 1
            return

        currnode = self.head
        while currnode.nextNode :
            currnode = currnode.nextNode
        
        currnode.nextNode = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        if index<0 or index>self.size :
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        
        currNode = self.head
        newNode = Node(val)
        index = index - 1
        while index:
            currNode = currNode.nextNode    #prev Node
            index -= 1
        
        temp = currNode.nextNode
        currNode.nextNode = newNode
        newNode.nextNode = temp

        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        
        if index<0 or index>self.size-1 :
            return

        curr = self.head
        if index == 0:
            self.head = curr.nextNode
        else:
            for i in range(index - 1):
                curr = curr.nextNode
            curr.nextNode = curr.nextNode.nextNode

        self.size -= 1 

'''
["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
'''

linkedList = MyLinkedList() # Initialize empty LinkedList
linkedList.addAtHead(2)
linkedList.deleteAtIndex(1)
linkedList.addAtHead(2)
linkedList.addAtHead(7)
linkedList.addAtHead(3)
linkedList.addAtHead(2)
linkedList.addAtHead(5)
linkedList.addAtTail(5)
print(linkedList.get(5))
linkedList.deleteAtIndex(6)
linkedList.deleteAtIndex(4)
