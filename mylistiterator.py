class MyListIterator:
    def __init__(self, head):
        self.curNode = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.curNode is None:
           raise StopIteration
        else: 
           data = self.curNode.data
           self.curNode = self.curNode.next
        return data
