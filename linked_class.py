from linked_list import MyList, ListNode

class MyQueue:
    def __init__(self):
        self.items = MyList()

    def length(self):
        return self.items.__len__()

    def isEmpty(self):
        if self.length() == 0:
            return True
        return False

    def enqueue(self, item):
        i = ListNode(item)
        self.items.add(i)


    def dequeue(self):
        if not self.isEmpty():
            data = self.items.get_item()
            return data

    def __iter__( self ):
        return self.items.__iter__()