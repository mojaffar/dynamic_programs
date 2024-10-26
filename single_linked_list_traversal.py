# Traversing using singly linked list
class Node:  # Creating a node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:  # Node is attribute of linkedlist
    def __init__(self):
        self.head = None

    def Traversal(self):  # Traversal through linked List
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next

    def Count_number_of_nodes(self):
        count = 0
        p = self.head
        while p is not None:
            count += 1
            p = p.next

        print(count)

    def Searching_an_element(self):
        x = 'Saturday'
        pos = 1
        p = self.head
        while p is not None:
            if p.data == x:
                print("Element found at: ", pos)
            pos += 1
            p = p.next
        else:
            print("Element is not available in given liked list")

    def Find_last_node_item(self):
        p = self.head
        while p.next is not None:
            p = p.next
        print(p.data)

    def Find_second_last_node_item(self):
        p = self.head
        while p.next.next is not None:
            p = p.next
        print(p.data)


list = SinglyLinkedList()

# Creating nodes
l1 = Node("Monday")
l2 = Node("Tuesday")
l3 = Node("Wednesday")
l4 = Node("Thursday")
l5 = Node("Friday")
l6 = Node("Saturday")
l7 = Node("Sunday")

# making first node as head node
list.head = l1

# Link first Node to second node
l1.next = l2
# Link second Node to third node
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

# list.Traversal()
# list.Count_number_of_nodes()
# list.Searching_an_element()
# list.Find_last_node_item()
# list.Find_second_last_node_item()

