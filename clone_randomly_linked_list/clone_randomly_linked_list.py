import random
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.data = int(x)
        self.next = next
        self.random = random

class LinkedList:
    
    # Function to initialize the Linked
    # List object
    def __init__(self, head=None):
        self.head = head

def copyRandomList(head):

    # Insert each node's copy right after it
    node = head
    while node:
        copy = Node(node.data)
        copy.next = node.next
        node.next = copy
        node = copy.next

    # Set each copy's .random
    node = head
    while node.random:
        node.next.random = node.random.next #and node.random.next
        node = node.next.next

    # Separate the copied list from the original, (re)setting every .next
    node = head
    copy_head = node.next
    copy = copy_head
    while copy.next is not None:
        copy.next = copy.next.next
        copy = copy.next

    return copy_head


#
#Function to create a linked list with random pointers to other items in the list
###
def create_rand_ll(n):
    llist = LinkedList()
    llist.head = Node(0)
    node = llist.head
    rand_set = set()
    while len(rand_set) < n:
        rand = random.randint(0, n)
        rand_set.add(rand)
    l = list(rand_set)
    random.shuffle(l)
    ll = []
    ll.append(node)

    for i in l:
        node.data = i
        node.next = Node(i)
        node = node.next
        ll.append(node)
    random.shuffle(l)
    node = llist.head
    
    for i in l:
        node.random = ll[i]
        node = node.next
    return llist.head



#
#Create and copy the list 
####
head = create_rand_ll(10)

copy = copyRandomList(head)

print("Original list")
while head:
    print(vars(head))
    if head.random:
        print(head.random.data)
    head = head.next

print("Copied list")    
while copy:
    print(vars(copy))
    if copy.random:
        print(copy.random.data)
    copy = copy.next

