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
printlinkedlist(head)
def insertion(head):
    newNode = Node(4)
    newNode.next = head
    head = newNode
    return head
head = insertion(head)
printlinkedlist(head)
def insertion(head):
    newNode = Node(1)
    curr = head
    while(curr.next!= None):
        curr = curr.next
    curr.next = newNode
    return head
head = insertion(head)
printlinkedlist(head) 
k = 3
newNode = Node(6)
curr = head
for i in range(k-1):
    curr= curr.next
newNode.next = curr.next
curr.next = newNode
printlinkedlist(head)
head = head.next
printlinkedlist(head)
curr = head
while(curr.next.next!=None):
    curr = curr.next
curr.next = None
printlinkedlist(head)