class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        # check for empty ll
        if not self.head:
            self.head = new_node
            return
        # if ll i snot empty then need to find last node to insert new node
        current = self.head
        while current.next is  not None:
            current = current.next

        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        if self.head is None:
            print("Link list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end="--->")
                current = current.next
            print()

    def count_nodes(self):
        count = 0
        current = self.head
        while current is not  None:
            count +=1
            current = current.next

        print("Total not of nodes in the ll: ", count)
        print()

    def search_element(self, element):
        current = self.head
        position = 1
        while current is not None:
            if current.data == element:
                print("Element found at position: ", position)
                break
            position +=1
            current = current.next

    def find_last_node(self):
        position = 1
        current = self.head

        if current is None:
            print("Linked list is empty")
        else:
            while current.next is not None:
                position +=1
                current = current.next

            print("Last node found at pos: ", position)
            print("Last node data: : ", current.data)

    def find_node_given_position(self, x):
        if x <= 0:
            print("Invalid position. Must be >= 1.")
            return

        position = 1
        current = self.head

        while position < x and current is not None:
            current = current.next
            position += 1

        if current is None:
            print(f"No node found at position {x}.")
        else:
            print(f"Stored data at position {x}: {current.data}")

    def find_node_data_in_given_pos(self, start, end):
        if start>end or start<=0:
            print("invalid input")

        current = self.head
        pos = 1
        temp = []
        while current is not None:
            if start<=pos<=end:
                temp.append(current.data)
            if pos>end:
                break

            current = current.next
            pos +=1
        return temp

    def second_last_node(self):
        current = self.head
        while current.next.next is not None:
            current = current.next

        print("Second last node data: ", current.data)

    def insert_node_between_nodes(self, node1):
        new_node = Node(25)
        if not self.head:
            return "Invalid ll, it means given nodes are not there"

        current = self.head
        while current is not None: # find exact node where to insert
            if current.data == node1:
                break
            current = current.next

        # inset node once we get where to store
        new_node.next = current.next
        current.next = new_node
        return None

    # first way to do
    def check_cyclic_link_list(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Cyclic link list")
                return True
        print("Not cyclic link list")
        return False
    # another way to do using hashset
    def has_cycle_set(self):
        visited =set()
        current = self.head
        while current is not None:
            if current in visited:
                print("cyclic detected")
                return True

            visited.add(current)
            current = current.next
        print("cyclic not detected")
        return False

    # remove cycle from ll
    # first detect cycle, 2nd find start of cycle and remove that cycle
    def remove_cycle(self):
        slow = self.head
        fast = self.head

        # check for cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # check for cycle
            if slow == fast:
                print("detected cycle")
                break

        else:
            print("not cycle detected")
            return

        # find start of cycle
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # remove cycle

        ptr = slow
        while fast.next !=ptr:
            fast = fast.next

        fast.next = None

        print("cyclic remove")


    def reverse_liked_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        print("printing reverse link list")
        self.head=prev
        return prev

    def delete_first_node(self):
        if not self.head:
            print("empty ll")
            return
        self.head =self.head.next

    def delete_last_node(self):
        if not self.head:
            print("ll is empty")
            return
        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next=None

    def again_reverse_ll(self):
        prev = None
        current = self.head
        while current is not None:
            temp_next_node = current.next
            current.next = prev
            prev = current
            current = temp_next_node

        self.head = prev

    def delete_node_20_30(self):
        if not self.head:
            print("empty ll")
            return
        current = self.head
        while current is not None:
            if current.data == 20:
                break
            current = current.next
        current.next = current.next.next

    def sort_link_list_using_bubble_sort(self):
        if not self.head:
            print("empty ll")
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def reorder_link_list(self):
        if not self.head:
            return

        nodes_data = []
        current = self.head
        # store all the data into list
        while current:
            nodes_data.append(current)
            current = current.next

        # take two pointes
        i, j = 0, len(nodes_data)-1

        # alternative the pointers basically reordering it
        while i<j:
            nodes_data[i].next = nodes_data[j]
            # increment of i value by 1
            i+=1
            if i>j:
                break
            nodes_data[j].next = nodes_data[i]
            j-=1

        # setting next of middle node to None
        nodes_data[i].next = None

    def remove_nth_node_from_end(self, n):
        if not self.head:
            return

        # Step 1: Count number of nodes
        pos = 0
        current = self.head
        while current is not None:
            current = current.next
            pos += 1

        # Step 2: If n == total number of nodes → Remove head
        if n == pos:
            self.head = self.head.next
            return

        # Step 3: Find node BEFORE the one to remove
        node_to_remove = pos - n
        current = self.head
        i = 1
        while i < node_to_remove:
            current = current.next
            i += 1

        # Step 4: Remove node
        if current.next:
            current.next = current.next.next

        return self.head

    def remove_nth_node_two_pointers(self, n):
        if not self.head:
            return

        slow = fast = self.head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return self.head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return self.head



    def remove_nth_node_from_start(self, n):

        if not self.head:
            return

        if n == 1:
            self.head = self.head.next
            return self.head.next

        current = self.head
        pos = 1
        while pos<n:
            current = current.next
            pos+=1

        if current.next:
            current.next = current.next.next

        return self.head

ll = SingleLinkedList()
ll.insert_at_end(20)
ll.insert_at_end(10)
ll.insert_at_end(40)
ll.insert_at_end(30)
ll.insert_at_end(50)
ll.traverse()

ll.count_nodes()

# search an element in the linked list
ll.search_element(30)

# find last node details
ll.find_last_node()

# find node details at given position x
ll.find_node_given_position(3)
ll.find_node_given_position(6) # after last node whatever you give positon it will give you value of last position only


# list of all the node data in given position
value = ll.find_node_data_in_given_pos(2,3)
if value:
    print(value)


# find second last node value
ll.second_last_node()

# insert at beginning
ll.insert_at_beginning(100)
ll.traverse()

# Insert a node b/w two nodes -20, 30 So basically after 20 need to insert

ll.insert_node_between_nodes(20)
ll.traverse()

# check for cyclic link list two ways to do
# ll.check_cyclic_link_list()
ll.has_cycle_set()
ll.remove_cycle()

# reverse link list
ll.reverse_liked_list()
ll.traverse()

# delete first node
# ll.delete_first_node()
# ll.traverse()

# delete last node
# ll.delete_last_node()
# ll.traverse()
#
# ll.again_reverse_ll()
# ll.traverse()

# delete node in b/w
# ll.delete_node_20_30()
# ll.traverse()


# sort using bubble
ll.sort_link_list_using_bubble_sort()
ll.traverse()

# # reorder link list
# ll.reorder_link_list()
# ll.traverse()

# # remove nth node form the end, using position calculation
# ll.remove_nth_node_from_end(1)
# ll.traverse()


# remove nth node from the start

ll.remove_nth_node_from_start(1)
ll.traverse()

ll.remove_nth_node_two_pointers(3)
ll.traverse()





























