import numpy as np
import datetime
import time
import mmcSim
import grocerySim

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
        self.wait_time =wait_time
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
    def get_payment_type(self):
        return self.payment_type
    def get_wait_time(self):
        return self.wait_time
    def get_service_time(self):
        return self.service_time

def findAvgArrivalTime(lane):
    flag = 0
    elems = []
    t1 = 0
    for i in lane:
        if not(flag==0):
            t = i.get_arrival_time()
            t2 = t1
            t1 = datetime.datetime.strptime(t,"%H:%M:%S")
        if flag>1:
            t3 = t1 - t2
            # print(t3)
            elems.append(t3.seconds)
        flag+=1

    m = np.mean(elems)
    return m

def findAvgServiceTime(lane):
    flag = 0
    elems = []
    t1 = 0
    for i in lane:
        if not(flag==0):
            t = i.get_service_time()
            if not(t=='0'):
                t1 = time.strptime(t,"%M:%S")
                t1 = t1.tm_min*60 + t1.tm_sec
                elems.append(t1)
        flag+=1
    m = np.mean(elems)
    # print(elems)
    return m

def findArrivalRate(lane):
    n = len(lane)

    rate = n/30 # arrival rate / length of people in queue divide total time in queue
    return rate


def findServiceRate(lane):
    m = findAvgServiceTime(lane)
    n = len(lane)
    n -= 1
    rate = 1/(m/n)
    return rate

out_file = open('output.txt','w')
def main():




    print("",file=out_file)
    lane=[]

    datalist = read_from_file("Data/Express.csv")
    lane.append(datalist)
    datalist = read_from_file("Data/KerschelJonathan.csv")
    lane.append(datalist)
    datalist = read_from_file("Data/KerschelSanjay.csv")
    lane.append(datalist)
    datalist = read_from_file("Data/RondellGerard.csv")
    lane.append(datalist)
    datalist = read_from_file("Data/SachinJonathan.csv")
    lane.append(datalist)
    datalist = read_from_file("Data/SachinSanjay.csv")
    lane.append(datalist)

    arrival = findArrivalRate(lane[0])
    service = findServiceRate(lane[0])

    print("MASSY STORE THAT WE SURVERYED",file=out_file)

    print ("Summary results of express lane:",file=out_file)
    express=mmcSim.QSim(service,arrival,1,300,out_file)
    print("",file=out_file)

    sumArrival=0
    sumService=0
    for i in range(1,len(lane)):
        sumArrival += findArrivalRate(lane[i])
        sumService += findServiceRate(lane[i])

    avgArrival=sumArrival/len(lane)
    avgService=sumService/len(lane)
    print ("Summary results of general lanes (lanes: {}):".format(len(lane)-1),file=out_file)
    general=mmcSim.QSim(avgService,avgArrival,len(lane),300,out_file)


    print("",file=out_file)

    print("SIMULATION OF GROCERY TO FIND IDEAL NUMBER OF SERVERS",file=out_file)
    grocerySim.mainSim(arrival,service,sumArrival,sumService,out_file)

    print("",file=out_file)
    print("--ACTUAL GROCERY SUMMARY--",file=out_file)
    print("Total costs from both express lanes and general lanes %.2f" % (express['totalCost'][0] + general['totalCost'][0]),file=out_file)
    print("And the amount of servers were 6 (including 1 express lane)",file=out_file)

main()

