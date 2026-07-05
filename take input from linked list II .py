class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print__ll(head):
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

newhead = take_input()
print__ll(newhead)