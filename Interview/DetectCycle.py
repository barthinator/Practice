class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
    def __str__(self):
     return self.data

def has_cycle(head):
    # Set our default variables
    first = second = head
    if head is None:
        return False
    # Basically whenever any of the elements are none it ends
    while (first and second and second.next):
        first = first.next
        second = second.next.next
        if first == second:
            return True

list = Node("test", Node("test1"))
# Makes the list circular
# list.next = list
print(has_cycle(list))
