"""
each minute a server is idle costs us  $15
each minute a customer waits for a server costs us $20
"""
"""
Total cost of idle server per minute = (100- utilization ) * #2
Total cost of customer waiting per minute = Lq * 100 * #2
Add both cost
"""

import random
import csv
import numpy as np
from collections import defaultdict


#define a class called 'Customer'
class Customer:
    def __init__(self,arrival_time,service_start_time,service_time):
        self.arrival_time=arrival_time
        self.service_start_time=service_start_time
        self.service_time=service_time
        self.service_end_time=self.service_start_time+self.service_time
        self.wait=self.service_start_time-self.arrival_time

#a simple function to sample from negative exponential
def neg_exp(lambd):
    return random.expovariate(lambd)

def sample_disc_uniform(a, b):
    u = np.random.uniform(0, 1) # sample from Uniform(0, 1)
    diff = b - a # get max length possible
    distance = diff * u  # travel a fraction of that length
    return int((a + distance)) # go that far away from min value

def QSim(lambd,mu,servers,simulation_time):
    """
    This is the main function to call to simulate an MM1 queue.
    """
    #Initialise clock
    t=0

    #Initialise empty list to hold all data
    Customers=defaultdict(list)

#----------------------------------
#The actual simulation happens here:
    while t<simulation_time:
        #randomly choose a server to go to
        choice=sample_disc_uniform(0,servers)

        #calculate arrival date and service time for new customer
        if (len(Customers[str(choice)])==0):

            arrival_time=neg_exp(lambd)
            service_start_time=arrival_time
        else:

            arrival_time+=neg_exp(lambd)
            service_start_time=max(arrival_time,Customers[str(choice)][-1].service_end_time)
        service_time=neg_exp(mu)

        #create new customer
        Customers[str(choice)].append(Customer(arrival_time,service_start_time,service_time))

        #increment clock till next end of service
        t=arrival_time
#----------------------------------

    #calculate summary statistics
    numCustomers=0
    for i in range(servers):
        numCustomers=numCustomers+len(Customers[str(i)])

    Mean_Wait=0
    for i in range(servers):
        customers=Customers[str(i)]
        Waits=[a.wait for a in customers]
        if(len(Waits)==0):
            Mean_Wait=0
        else:
            Mean_Wait=Mean_Wait+sum(Waits)/len(Waits) #W

    #find average by amoutn of servers
    Mean_Wait=Mean_Wait/servers

    Mean_Time=0
    for i in range(servers):
        customers=Customers[str(i)]
        Total_Times=[a.wait+a.service_time for a in customers]
        if(len(Total_Times)==0):
            Mean_Time=0
        else:
            Mean_Time=Mean_Time+sum(Total_Times)/len(Total_Times) #WQ

    #find average by amoutn of servers
    Mean_Time=Mean_Time/servers

    Mean_Service_Time=0
    Service_Times_Sum=0
    for i in range(servers):
        customers=Customers[str(i)]
        Service_Times=[a.service_time for a in customers]
        if(len(Service_Times)==0):
            Mean_Service_Time=0
        else:
            Mean_Service_Time=Mean_Service_Time+sum(Service_Times)/len(Service_Times)

        Service_Times_Sum=Service_Times_Sum+sum(Service_Times)

    #find average by amoutn of servers
    Mean_Service_Time=Mean_Service_Time/servers

    Utilisation=Service_Times_Sum/t #P

    Queue_Length=0
    for i in range(servers):
        customers=Customers[str(i)]
        Service_Wait=[a.wait for a in customers]
        Queue_Length=Queue_Length+sum(Service_Wait)/t

    #find average by amoutn of servers
    Queue_Length=Queue_Length/servers



    #output summary statistics to screen
    print ("")
    print ("Summary results:")
    print ("")
    print ("Number of customers: ",numCustomers)
    print ("Mean Service Time: ",Mean_Service_Time)
    print ("Mean Wait: ",Mean_Wait)
    print ("Mean Time in System: ",Mean_Time)
    print ("Utilisation: ",Utilisation)
    print ("Queue_Length: ",Queue_Length)
    print ("")

    #return total cost
    return

