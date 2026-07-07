class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):
    temp = head
    while temp != None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

def take_input():
    value = int(input("Enter the value of Node: "))
    head = None

    while value != -1:
        newNode = Node(value)

        if head == None:
            head = newNode
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

        value = int(input("Enter the value of Node: "))

    return head
head = take_input()
print_ll(head)
def insert_at_head(head,data):
    newNode =Node(data)
    newNode.next=head
    head = newNode
    return head
head = insert_at_head(head,100)
print("after inserting at head")
print_ll(head)