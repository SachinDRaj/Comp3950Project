import mmcSim
import numpy as np


# out_file = open('output.txt','a')

def mainSim(arrivalExpress,serviceExpress,arrivalGeneral,serviceGeneral,out_file):
    #constants
    leastServers=10
    mostServers=20

    #chosen mu and lambd from grocery surverying on a the peak hrs in a specific day
    muGeneral=serviceGeneral
    lambdGeneral=arrivalGeneral
    muExpress=serviceExpress
    lambdExpress=arrivalExpress

    Customers=[]
    count=0

    print("Express Lane: ",file=out_file)
    expressData=mmcSim.QSim(muExpress,lambdExpress,1,300,out_file)

    print("",file=out_file)
    print("--General Lane Summary: --",file=out_file)
    for i in range(leastServers,mostServers+1):
        count=count+1
        print("Amount of servers: ",i,file=out_file)
        Customers.append(mmcSim.QSim(muGeneral,lambdGeneral,i,300,out_file))
        print("",file=out_file)

    cost=[]
    for i in range(count):
        cost.append(Customers[i]['totalCost'][0] + expressData['totalCost'][0])

    print("",file=out_file)
    for i in range(50):
        print("*",end='',file=out_file)
    print("",file=out_file)

    #add the total cost of the express lane to the total cost of the accumulated general lanes
    print("--SIMULATION SUMMARY--",file=out_file)
    count=0
    print("%s\t%s\t%s"%("ID","Servers","Cost ($)"),file=out_file)
    for i in range(leastServers,mostServers+1):
        count=count+1
        print("%d\t%d\t\t%.2f" % (count,i,cost[count-1]),file=out_file)

    #find minimum cost of array
    minCost=np.amin(cost)
    minLoc=np.argmin(cost)
    print("\nThe minimum cost from both express lanes and general lanes: $%.2f\nand the amount of servers were %d (including 1 express lane)"%(minCost,leastServers+minLoc),file=out_file)

    return
