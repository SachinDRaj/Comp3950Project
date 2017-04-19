import mmcSim
import numpy as np

#constants
leastServers=10
mostServers=20

#chosen mu and lambd from grocery surverying on a the peak hrs in a specific day
mu=10
lambd=20

Customers=[]
count=0
for i in range(leastServers,mostServers+1):
    count=count+1
    print("Amount of servers: ",i)
    Customers.append(mmcSim.QSim(mu,lambd,i,300))
    print("")

cost=[]
for i in range(count):
    cost.append(Customers[i]['totalCost'][0])

print("")
for i in range(50):
    print("*",end='')
print("")

count=0
print("{}\t{}\t{}".format("ID","Servers","Cost ($)"))
for i in range(leastServers,mostServers+1):
    count=count+1
    print("{}\t{}\t{:.4}".format(count,i,cost[count-1]))

#find minimum cost of array
minCost=np.amin(cost)
minLoc=np.argmin(cost)
print("\nThe minimum cost for the given data is: ${:.4}\nand the amount of servers were {}".format(minCost,leastServers+minLoc))


