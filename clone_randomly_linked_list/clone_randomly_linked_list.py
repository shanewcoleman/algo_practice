import random
class Node:
    def __init__(self, x = None, next: 'Node' = None, random: 'Node' = None):
        self.data = x
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
    while node and node.random:
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
    llist.head = Node()
    node = llist.head
    rand_set = set() # Initialize set data structure so we don't get duplicate items
    while len(rand_set) < n: # Make sure the set has the appropirate number of items
        rand = random.randint(0, n)
        rand_set.add(rand)
    l = list(rand_set)
    random.shuffle(l) #Shuffle our list so the data isn't ordered and boring
    ll = [] # Our data structure here is going to be a list of linked lists, that way we have an index to point to for our .random creation
    ll.append(node)

    for i in l:
        node.next = Node()
        node.data = i
        node = node.next
        ll.append(node) # We've created the nodes and added them to our list
    random.shuffle(l) # Shuffle it up again so we can point to random elements in our list
    node = llist.head
    
    for i in l:
        node.random = ll[i]#Each element in l points to a random node now, so the .random will in fact point to a random item in the linked list
        node = node.next
    return llist.head



#
#Create and copy the list 
####
head = create_rand_ll(7)

copy = copyRandomList(head)

print("Original list")
while head:
    print(vars(head))
    if head.random:
       print(head.next.data)
    head = head.next

print("Copied list")    
while copy:
    print(vars(copy))
   # if copy.random:
    #    print(copy.random.data)
    copy = copy.next

