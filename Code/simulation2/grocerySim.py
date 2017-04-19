import mmcSim
import numpy as np

#constants
leastServers=10
mostServers=20

#chosen mu and lambd from grocery surverying on a the peak hrs in a specific day
muGeneral=10
lambdGeneral=20
muExpress=11
lambdExpress=20

Customers=[]
count=0

print("Express Lane: ")
expressData=mmcSim.QSim(muExpress,lambdExpress,1,300)

print("--General Lane Summary: --")
for i in range(leastServers,mostServers+1):
    count=count+1
    print("Amount of servers: ",i)
    Customers.append(mmcSim.QSim(muGeneral,lambdGeneral,i,300))
    print("")

cost=[]
for i in range(count):
    cost.append(Customers[i]['totalCost'][0] + expressData['totalCost'][0])

print("")
for i in range(50):
    print("*",end='')
print("")

#add the total cost of the express lane to the total cost of the accumulated general lanes

count=0
print("%s\t%s\t%s"%("ID","Servers","Cost ($)"))
for i in range(leastServers,mostServers+1):
    count=count+1
    print("%d\t%d\t%.2f" % (count,i,cost[count-1]))

#find minimum cost of array
minCost=np.amin(cost)
minLoc=np.argmin(cost)
print("\nThe minimum cost for the given data is: $%.2f\nand the amount of servers were %d"%(minCost,leastServers+minLoc))


