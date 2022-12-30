#write a code for a priority queue using a a linkedlist

class node:
    def __init__(self,data):

        self.next = None
        self.data = data

class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,value):
        new_node= node(value)

        if self.head == None:
            self.head = new_node
            return None
        cur_node = self.head
        while cur_node:
            if cur_node.next==None:
                new_node = node(value)
                cur_node.next = new_node
                break
            cur_node = cur_node.next

    def peep(self):
         if self.head == None:
             print(None)
             return 
         print(self.head.data)

    def pop(self):
        if self.head == None:
            return None

        print(self.head.data)
        self.head = self.head.next

    def viewnode(self):
        if self.head == None:
            print('The list is empty')
            return None
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


#testing

llist = linkedlist()
llist.insert(10)
llist.insert(30)
llist.insert(30)
llist.pop()
llist.pop()
print()
llist.viewnode()

            
        
        
            
