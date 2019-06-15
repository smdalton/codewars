
class Node:
    def __init__(self, next_node=None, data=None):
        self.next = next_node
        self.data = data


node1 = Node(data=1)
node2 = Node(data=2)
node3 = Node(data=3)
node4 = Node(data=4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2



head = node1
cycle_head = None
start = True
current_node = node1
runner_node = node1


def find_cycle(head):
    i = 0  # infinite loop prevention
    cycle_head = None
    start = True
    current_node = head
    runner_node = head
    while current_node.next and i < 5:
        current_node = current_node.next
        runner_node = runner_node.next.next
        if(current_node == runner_node):
            len = count_cycle_length(current_node)
            return len
    return False

def count_cycle_length(cycle_head):
    current = cycle_head.next
    len = 1
    while current != cycle_head:
        current = current.next
        len += 1
    return len

print(find_cycle(head))