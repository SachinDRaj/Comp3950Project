import numpy
import time

def read_from_file(filepath):
    in_file = open(filepath,'r')
    contents = in_file.read()
    in_file.close()
    return get_from_string(contents)

def get_from_string(contents):
    datalist = []
    all_lines = contents.split('\n')
    for line in all_lines:
        line = line.split(',')
        cus_no = line[0].strip()
        arrival_time = line[1].strip()
        service_start = line[2].strip()
        service_end = line[3].strip()
        drop_time = line[4].strip()
        n_items = line[5].strip()
        payment_type = line[6].strip()
        wait_time = line[7].strip()
        service_time = line[8].strip()
        datalist.append(Customer(cus_no,arrival_time,service_start,service_end,drop_time,n_items,payment_type,wait_time,service_time))
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
    def __init__(self, customer_no, arrival_time, service_start_time, service_end_time, drop_time, number_items, payment_type, wait_time, service_time):
        self.customer_no = customer_no
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

    def get_arrival_time(self):
        return self.arrival_time
    def get_customer_no(self):
        return self.customer_no
    def get_service_start_time(self):
        return self.service_start_time
    def get_service_end_time(self):
        return self.service_end_time
    def get_drop_time(self):
        return self.drop_time
    def get_number_items(self):
        return self.number_items


datalist=read_from_file("Data/Express.csv")
cust = datalist[1].get_arrival_time()

struct_time = time.strptime(cust,"%H:%M:%S")

print(struct_time)

# print(struct_time)