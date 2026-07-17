class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next      
            curr.next = prev    
            prev = curr          
            curr = nxt           
        return prev
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for value in arr[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
values = list(map(int, input("Enter elements: ").split()))
head = createLinkedList(values)
print("Original Linked List:")
printLinkedList(head)
solution = Solution()
head = solution.reverseList(head)
print("Reversed Linked List:")
printLinkedList(head)