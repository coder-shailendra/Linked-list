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
def lengthofLL(head):
    temp =head
    ans=0
    while(temp!=None):
        temp = temp.next
        ans = ans+1
    return ans
headofLL=take_input()
length = lengthofLL(headofLL)
print(length)
def lengthoflinkedlistrecursive(head):
    if (head == None):
        return 0
    recursive_ans = lengthoflinkedlistrecursive(head.next)
    return 1+recursive_ans
length = lengthoflinkedlistrecursive(headofLL)
print(length) 