import random
import csv


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


def QSim(lambd,mu,simulation_time):
    """
    This is the main function to call to simulate an MM1 queue.
    """
    
    #Initialise clock
    t=0

    #Initialise empty list to hold all data
    Customers=[]

#----------------------------------
#The actual simulation happens here:
    while t<simulation_time:

        #calculate arrival date and service time for new customer
        if len(Customers)==0:
            arrival_time=neg_exp(lambd)
            service_start_time=arrival_time
        else:
            arrival_time+=neg_exp(lambd)
            service_start_time=max(arrival_time,Customers[-1].service_end_time)
        service_time=neg_exp(mu)

        #create new customer
        Customers.append(Customer(arrival_time,service_start_time,service_time))

        #increment clock till next end of service
        t=arrival_time
#----------------------------------

    #calculate summary statistics
    Waits=[a.wait for a in Customers]
    Mean_Wait=sum(Waits)/len(Waits) #W

    Total_Times=[a.wait+a.service_time for a in Customers]
    Mean_Time=sum(Total_Times)/len(Total_Times) #WQ

    Service_Times=[a.service_time for a in Customers]
    Mean_Service_Time=sum(Service_Times)/len(Service_Times)

    #print(Service_Times)

    Utilisation=sum(Service_Times)/t #P

    Service_Wait=[a.wait for a in Customers]
    Queue_Length=sum(Service_Wait)/t



    #output summary statistics to screen
    print ("")
    print ("Summary results:")
    print ("")
    print ("Number of customers: ",len(Customers))
    print ("Mean Service Time: ",Mean_Service_Time)
    print ("Mean Wait: ",Mean_Wait)
    print ("Mean Time in System: ",Mean_Time)
    print ("Utilisation: ",Utilisation)
    print ("Queue_Length: ",Queue_Length)
    print ("")

    return


def simulateGrocery(nServers, eServers,simulation_time,lambd,mu):

    for i in range(nServers):
        print("")
        print("Summary Results for lane", i)
        print("")
        QSim(lambd,mu,simulation_time)

    for i in range(eServers):
        print("")
        print("Summary Results for lane", i)
        print("")
        QSim(lambd,mu,simulation_time)


    return

def simulateG():

    total_time = 60
    n = int(total_time/30);

    lambd = 2
    mu = 3
    nServers = 5
    eServers = 1

    for i in range(n):
        simulateGrocery(nServers,eServers,30,lambd,mu)

simulateG()
