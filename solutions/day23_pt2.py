



class Node:
    def __init__(self, n):
        self.n = n
        self.next = None


def printlist(node):
    endval = node.n
    node = node.next
    print(endval, end = "->")
    while node.n != endval:
        print(node.n, end = "->")
        node = node.next
    print("\n\n")



if __name__ == '__main__':
    cups = "496138527"
    cups = [int(i) for i in cups]
    node_lookup = {}
    
    # make linked list
    head = Node(int(cups[0]))
    node_lookup[int(cups[0])] = head
    current = head
    for i in cups[1:]:
        current.next = Node(int(i))
        node_lookup[int(i)] = current.next
        current = current.next
    

    for i in range(10, 1000001):
        current.next = Node(i)
        node_lookup[int(i)] = current.next
        current = current.next
    current.next = head
    #printlist(head)

    for i in range(10000000):
        # if i%1000 == 0:
        #     print(i)
        current = head
        a = current.next
        b = a.next
        c = b.next
        next_head = c.next

        current.next = next_head

        dest = current.n-1
        a_val = a.n
        b_val = b.n
        c_val = c.n

        while dest in {a_val, b_val, c_val,0}:
            dest-=1
            if dest<=0:
                dest = 1000000
        
        dest_node = node_lookup[dest]

        # insert a,b,c to list after dest
        tmp = dest_node.next
        dest_node.next = a
        c.next = tmp
        head = next_head
    #print("\n\n\n")
    #printlist(head)
    print(f"Ans 2: {node_lookup[1].next.n * node_lookup[1].next.next.n}")






