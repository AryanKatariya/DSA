import queue

# inbuilt queue library
q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

while not q.empty():
    print(q.get())

p = queue.LifoQueue()
p.put(1)
p.put(2)
p.put(3)
while not p.empty():
    print(p.get())
