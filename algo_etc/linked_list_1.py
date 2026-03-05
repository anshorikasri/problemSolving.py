#start: 25.02.2026
# title: Manually making Linked List

# === === === ===

# step 1 - define a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# our target is to make the linked list like this:
# 1 -> 2 -> 4 -> 'Sha' -> True -> 'AI'

# we do instance the 'Node' class
n1 = Node(1) 
n2 = Node(2)
n3 = Node(4)
n4 = Node('Sha')
n5 =  Node(True)
n6 = Node('AI')


# next, we link them all as node
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

# here, we does not have the head
# we need to declare the head
head = n1



# i am sorry if any wrong in my video. see you later :)

print(n5.next)