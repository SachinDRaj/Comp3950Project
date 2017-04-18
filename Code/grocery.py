"""
groceryQueue: general queue of grocery (arrival rate x)
expressQueue[]: express queues (for 10 items or less)
generalQueue[]: general queue for any amount of items

process:
    -decide the amount  of servers available depend on
        the groceryQueue arrival rate as seen for 30 mins
    -decide which queue to enter IMMEDIATELY as a customer arrives
        what influences choice
            current length of each queue from the servers available
            the expected service time of all customers in the queue (this is exponentially distributed, but it directly correlates with the number of items in the customers cart. For this reason, a random number of items will not be generated for each customer, instead, the expected service time will be used)
    -decide if to drop from a queue and enter another queue
        condition: 
            The expected wait time of the current time is higher than the expected wait time of anothe line
            AND the amount of customers served in both queues, since the customer entered their queue, is different. Where the amount of customers left favors the next queue

expected results:
    as groceryQueue arrival rate increases, the amount of servers must increase to accomodate the customers. (This is done to ensure the average customer wait time remains at a suitable wait time. To the customer, time is money, should the customer need to wait too long to make their purchases, they would consider shopping else where, where better service is given)
    
    therefore the max number of servers necessary should account for peak time (usually refers to the end of the month after 3pm)
    Once the max number of servers is set, less servers can be allocated on days where there is no peak time
    
    can work on if there is time (future work)
        the average number of generalQueue should be found (not peak hrs)
        the average number of expressQueue should be found (not peak hrs)
        
        when exactly is peak hrs based on a csv file (most likely never doing this )
    
currently implemented:
    9 (general) servers are allowed at max, where less servers are allocated at any point in time 
    1 (express) server is allowed at max, where, as far as we saw, is always active 
    
during data gathering:
    1 (express ) server was active 
    5 (general) servers was active 
    
    both cases were recorded (3pm Wednesday 29 March 2017)
    
from data gathering
    for the 5 (general) servers that was active abd the 1 (express) server, the average arival rate for all servers were added. This became the average general queue arrival rate 
    
what was not considered:
    the atitude of any particular cashier or cashiers that changed due to shifts
    shopping time taken
"""

