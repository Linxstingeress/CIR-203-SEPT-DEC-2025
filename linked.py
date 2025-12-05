node3 = {
    "value": 30,
    "next": None     
}
node2 = {
    "value": 20,
    "next": node3    
}
node1 = {
    "value": 10,
    "next": node2    
}
linked_list = node1
def traverse_list(head):
    current = head
    while current is not None:
        print(current["value"])
        current = current["next"]
print("Linked List values:")
traverse_list(linked_list)
