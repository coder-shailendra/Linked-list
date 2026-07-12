class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Node(5)
b = Node(3) 
c = Node(7)  
a.next = b
b.next = c
head = a
print(head.data)
print(head.next.data)
print(head.next.next.data)
def printlinkedlist(head):
    curr = head
    while curr != None:
        print(curr.data , end="->")
        curr = curr.next
    print("None")
print("Before Insertion:")
printlinkedlist(head)
def insertion(head):
    newNode = Node(4)
    newNode.next = head
    head = newNode
    return head
head = insertion(head)
print("After Insertion:")
printlinkedlist(head)
