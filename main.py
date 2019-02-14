from linked_class import MyQueue
from myclass import my_point, my_point_child

a = my_point(1,2)
b = my_point(4,5)
c = my_point_child(1,5,8)
d = my_point_child(4,8,6)

q = MyQueue()
q.enqueue(2)
q.enqueue(a)
q.enqueue(b)
q.enqueue(c)
q.enqueue(d)
q.enqueue(4)
q.enqueue(5)

print('Queue lenght:', q.length())

print('Result of the dequeue() method: ', q.dequeue().get_data())
print('Result of the dequeue() method: ', q.dequeue().get_data().get_value())

print('Queue lenght:', q.length())

print(q.isEmpty())

if not q.isEmpty():
    for i in q:
        if isinstance(i, int):
            print(i)
        else:
            print(i.get_value())