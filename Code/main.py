import numpy

def read_from_file(filepath):
    in_file = open(filepath,'r')
    contents = in_file.read()
    in_file.close()
    return get_from_string(contents)

def get_from_string(contents):
    datalist = []
    all_lines = contents.split('\n')
    for line in all_lines:
        split = line.strip().split()
        u = split[0].strip()
        v = split[1].strip()
        w = float(split[2].strip())
        datalist.append((u, v, w))
    return datalist

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
