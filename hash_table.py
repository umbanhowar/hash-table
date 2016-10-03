class HashMap:
    def __init__(self, size):
        self.table = [Bucket() for i in xrange(0, size)]
        self.size = size
        self.count = 0
    def set(self, key, value):
        bucket = hash(key) % self.size
        if self.table[bucket].contains(key):
            self.table[bucket].set((key, value))
            return True
        else:
            if self.count == self.size:
                return False
            else:
                self.table[bucket].set((key, value))
                self.count += 1
                return True

    def get(self, key):
        bucket = hash(key) % self.size
        return self.table[bucket].get(key)
    def delete(self, key):
        bucket = hash(key) % self.size
        return self.table[bucket].remove(key)
    def load(self):
        return float(self.count) / self.size

class Bucket:
    """
    Class Bucket implements a singly-linked list to store Node((key, object reference))
    pairs in case of hash collisions.
    """
    def __init__(self):
        self.head = None
        self.length = 0
    def set(self, pair):
        """
        Set returns True if a NEW node was added, and False if an old node's value changed
        """
        if not self.head:
            self.head = Node(pair)
            self.head.next = None
            self.length += 1
            return True
        else:
            curr = self.head
            while curr != None:
                if curr.val[0] == pair[0]:
                    curr.val = (curr.val[0], pair[1])
                    return False
                curr = curr.next
            old_head = self.head
            self.head = Node(pair)
            self.head.next = old_head
            self.length += 1
            return True
    def get(self, key):
        curr = self.head
        while curr != None:
            if curr.val[0] == key:
                return curr.val[1]
            curr = curr.next
        return None
    def remove(self, key):
        curr = self.head
        while curr != None:
            if curr.val[0] == key:
                #check to see if this really works
                to_return = curr.val[1]
                curr.val = curr.next.val
                curr.next = curr.next.next
                self.length -= 1
                return to_return
            curr = curr.next
        return None
    def contains(self, key):
        """
        Returns true if the bucket contains the key, false otherwise
        """
        curr = self.head
        while curr != None:
            if curr.val[0] == key:
                return True
            curr = curr.next
        return False



class Node:
    """
    Class Node represents a node in a singly-linked list that will store a (key, object) tuple
    and a next pointer
    """
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return 'Node[val:' + self.val + ', next:' + self.next + ']'


                