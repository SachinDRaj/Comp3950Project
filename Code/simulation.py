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

    print ("Summary results:")
    print ("\tNumber of customers: ",len(Customers))
    print ("\tMean Service Time: %.2f"% Mean_Service_Time)
    print ("\tMean Wait: %.2f"%Mean_Wait)
    print ("\tMean Time in System: %.2f"%Mean_Time)
    print ("\tUtilisation: %.2f"%Utilisation)
    print ("\tQueue_Length: %.2f"%Queue_Length)

    idleCost = (1 - Utilisation) * 15
    waitingCost = Queue_Length * 100 * 20
    totalCost = idleCost+waitingCost
    print("\tWaiting cost: $%.2f" % waitingCost)
    print("\tIdle cost: $%.2f" % idleCost)
    print("\tTotal Cost: $%.2f" % totalCost)

    return len(Customers),Mean_Service_Time,Mean_Wait,Mean_Time,Utilisation,Queue_Length,idleCost,waitingCost,totalCost


def simulateGrocery(nServers, eServers,simulation_time,lambd,mu):

    nCus=0
    Mean_Service_Time=0
    Mean_Wait=0
    Mean_Time=0
    Utilisation=0
    Queue_Length=0

    for i in range(nServers):
        print("")
        print("Summary Results for lane", i)
        print("")
        nCus,Mean_Service_Time,Mean_Wait,Mean_Time,Utilisation,Queue_Length,idleCost,waitingCost,totalCost = QSim(lambd,mu,simulation_time)
        nCus+=nCus
        Mean_Service_Time+=Mean_Service_Time
        Mean_Wait+=Mean_Wait
        Mean_Time+=Mean_Time
        Utilisation+=Utilisation
        Queue_Length+=Queue_Length
        idleCost+=idleCost
        waitingCost+=waitingCost
        totalCost+=totalCost

    nCus=nCus/nServers
    Mean_Service_Time=Mean_Service_Time/nServers
    Mean_Wait=Mean_Wait/nServers
    Mean_Time=Mean_Time/nServers
    Utilisation=Utilisation/nServers
    Queue_Length=Queue_Length/nServers
    totalCost=totalCost/nServers

    # for i in range(eServers):
    #     print("")
    #     print("Summary Results for express lane")
    #     print("")
    #     nCus,Mean_Service_Time,Mean_Wait,Mean_Time,Utilisation,Queue_Length = QSim(lambd,mu,simulation_time)
    #     nCus+=nCus
    #     Mean_Service_Time+=Mean_Service_Time
    #     Mean_Wait+=Mean_Wait
    #     Mean_Time+=Mean_Time
    #     Utilisation+=Utilisation
    #     Queue_Length+=Queue_Length

    return

def simulateG():

    n=1

    lambd = 2
    mu = 3
    nServers = 5
    eServers = 1

    for i in range(n):
        simulateGrocery(nServers,eServers,30,lambd,mu)

simulateG()
