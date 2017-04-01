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
        arrival_time = split[0].strip()
        service_start = split[1].strip()
        service_end = split[2].strip()
        drop_time = split[3].strip()
        items = split[4].strip()
        card = split[5].strip()
        wait_time = split[6].strip()
        service_time = split[7].strip()
        # w = float(split[2].strip())
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

class Customer:
	def __init__(self, arrival_time, service_start_time, service_end_time, drop_time, number_items, payment_type, wait_time, service_time):
		self.arrival_time = arrival_time
		self.service_start_time = service_start_time
		self.service_end_time = service_end_time
		self.drop_time = drop_time
		self.number_items = number_items
		if payment_type == 0:
			self.payment_type = 'cash'
		elif payment_type == 1:
			self.payment_type = 'credit card'
		self.wait =wait_time
		self.service_time = service_time
