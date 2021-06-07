# using just arrays, direct access table
# using linked list for chaining

class Node:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0 # Keep track of number of objects stored in map
        self.capacity = 18 # length of list 
        self.map = [None]*self.capacity
        
    def hash(self, key):
        return key % self.capacity
         
    def resize(self):
        self.capacity <<= 1 #Shift the capacity left by a bit (so self.capacity * 2**1)
        new_map = [None] * self.capacity
        for i in range(self.capacity >> 1): #Going through the previous hash values and re-hashing all of the keys
            if self.map[i] is not None:
                n = self.hash(self.map[i])
                while new_map[n] is not None:
                    n = (5*n+1)%self.capacity #Avoid collisions by double-hashing, better than linear probe as linear probe iterates in O(n) time
                new_map[n] = self.map[i]
        self.map = new_map




    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.size / self.capacity >= float(2)/3:#Checking to see if the capacity is too high, if so, double the size to increase operational performance 
            self.resize()
        index = self.hash(key)
        if self.map[index] == None:
            self.map[index] = Node(key, value)
        else:
            item = self.map[index]
            while True:
                if item.pair[0] == key:
                    item.pair = (key, value) #update
                    return
                if item.next == None: break
                item = item.next
            item.next = Node(key, value)
        self.size += 1
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.hash(key)
        item = self.map[index]
        while item:
            if item.pair[0] == key:
                return item.pair[1]
            else:
                item = item.next
        return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self.hash(key)
        item = prev = self.map[index] # Keep track of current and previous items
        if not item: return
        if item.pair[0] == key:
            self.map[index] = item.next
        else:
            item = item.next
            while item: # Move through the list, if there's an item that matches what we want to remove, delete the pointers referencing it
                if item.pair[0] == key:
                    prev.next = item.next
                    break
                else:
                    item, prev = item.next, prev.next
