import mmcSim
import numpy as np

#constants
leastServers=10
mostServers=20

#chosen mu and lambd from grocery surverying on a the peak hrs in a specific day
mu=10
lambd=20

cost=[]
for i in range(leastServers,mostServers+1):
    cost.append(mmcSim.QSim(mu,lambd,i,300))

count=0

print("")
for i in range(50):
    print("*",end='')
print("")

print("{}\t{}\t{}".format("ID","Servers","Cost ($)"))
for i in range(leastServers,mostServers+1):
    count=count+1
    print("{}\t{}\t{:.4}".format(count,i,cost[count-1]))

#find minimum cost of array
minCost=np.amin(cost)
minLoc=np.argmin(cost)
print("\nThe minimum cost for the given data is: ${:.4}\nand the amount of servers were {}".format(minCost,leastServers+minLoc))


