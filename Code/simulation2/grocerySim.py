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

print(cost)

count=0
print("{}\t{}\t{}".format("id","servers","cost"))
for i in range(leastServers,mostServers+1):
    count=count+1
    print("{}\t{}\t{}".format(count,i,cost[count-1]))

#find minimum cost of array
minCost=np.amin(cost)
minLoc=np.argmin(cost)
print("The minimum cost for the given data is: {}\nand the amount of servers were".format(minCost,minLoc))


