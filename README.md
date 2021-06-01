# RAFTEscortSim

This project implemented “Escort simulator” using Raft consensus algorithm.

## Assumptions:

>There are n nodes in 2D (n ≥ 3) (nodes initialized on random coordinates)
>There is a flag at initial point (0, 0)
>One of the nodes should get the flag from (0, 0) to (100, 0) making 1 point step at a time
>Others should escort it keeping it in the center. If leading node is lost, one of the escorting should get to the last point of coordinator node was in and continue the trip.

## Steps for running this implementation:
Clone this repo, use `cd RaftEscortSim` (instead of `RaftEscortSim/RaftEscortSim/`)
### Run with virtual env without container:

1. Activate viturual env in `RaftEscortSim/RaftEscortSim/venv`
```shell
 source RAFTEscortSim/venv/bin/activate
```
Expected Output:
```shell
    (venv)john@laptop:~/RAFTEscortSim$ 
```
2. Start several server nodes in several individual termianl :
```shell
  python RaftEscortSim/nodes/ServerNode.py localtest1
```
```shell
  python RaftEscortSim/nodes/ServerNode.py localtest2
```
```shell
  python RaftEscortSim/nodes/ServerNode.py localtest3
```
Where `localtest1` is the `node_id` configured in `ClusterConfig.yaml`, this file inculdes the configuration infomation of our cluster, you may append new nodes by yourself.
```yaml
#Configuration of Cluster includes node Id and node IP address
# serverNodes:
#node_id:
#    ip:
#    port
localtest1:
  ip: 127.0.1.1
  port: 6387
localtest2:
  ip: 127.0.1.1
  port: 6388
localtest3:
  ip: 127.0.1.1
  port: 6386
```
Expected Output:
```shell
Subscriber socket on localtest1 connected tcp://127.0.1.1:6388
Subscriber socket on localtest1 connected tcp://127.0.1.1:6386
Publisher socket on localtest1 binded tcp://127.0.1.1:6387
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Timeout got no heartbeat on node localtest1,call election,CurrentTerm1
localtest1 calling election
VoteRequestResponse from localtest3,for localtest1,granted=True
localtest1 become leader, Term 1
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Votes_recived localtest1==>2/3
Node coordinates {'localtest1': (1, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (1, 0)}
Current:leaderlocaltest1
{'localtest1': (1, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (1, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (2, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (2, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 1
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 3
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 1
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 3
Node coordinates {'localtest1': (3, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (3, 0)}
Current:leaderlocaltest1
{'localtest1': (3, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (3, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (4, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (4, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 5
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 5
Node coordinates {'localtest1': (5, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (5, 0)}
Current:leaderlocaltest1
{'localtest1': (5, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (5, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (6, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (6, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 7
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 7
Node coordinates {'localtest1': (7, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (7, 0)}
Current:leaderlocaltest1
{'localtest1': (7, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (7, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (8, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (8, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 9
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 9
Node coordinates {'localtest1': (9, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (9, 0)}
Current:leaderlocaltest1
{'localtest1': (9, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (9, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (10, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (10, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 11
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 11
Node coordinates {'localtest1': (11, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (11, 0)}
Current:leaderlocaltest1
{'localtest1': (11, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (11, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (12, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (12, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 13
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 13
Node coordinates {'localtest1': (13, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (13, 0)}
Current:leaderlocaltest1
{'localtest1': (13, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (13, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (14, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (14, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 15
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 15
Node coordinates {'localtest1': (15, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (15, 0)}
Current:leaderlocaltest1
{'localtest1': (15, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (15, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (16, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (16, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 17
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 17
Node coordinates {'localtest1': (17, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (17, 0)}
Current:leaderlocaltest1
{'localtest1': (17, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (17, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (18, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (18, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 19
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 19
Node coordinates {'localtest1': (19, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (19, 0)}
Current:leaderlocaltest1
{'localtest1': (19, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (19, 0)}
localtest1 replicating_log to followers ,Current Term 1
Current:leaderlocaltest1
{'localtest1': (20, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (20, 0)}
localtest1 handling LogRP from localtest3 ,replicate success True ,        ack length 21
localtest1 handling LogRP from localtest2 ,replicate success True ,        ack length 21
```
```shell
Subscriber socket on localtest2 connected tcp://127.0.1.1:6387
Subscriber socket on localtest2 connected tcp://127.0.1.1:6386
Publisher socket on localtest2 binded tcp://127.0.1.1:6388
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (3, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (3, 0)}
Node coordinates {'localtest1': (5, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (5, 0)}
Node coordinates {'localtest1': (7, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (7, 0)}
Node coordinates {'localtest1': (9, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (9, 0)}
Node coordinates {'localtest1': (11, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (11, 0)}
Node coordinates {'localtest1': (13, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (13, 0)}
Node coordinates {'localtest1': (15, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (15, 0)}
Node coordinates {'localtest1': (17, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (17, 0)}
Node coordinates {'localtest1': (19, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (19, 0)}
Node coordinates {'localtest1': (21, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (21, 0)}
```
```shell
Subscriber socket on localtest3 connected tcp://127.0.1.1:6387
Publisher socket on localtest3 binded tcp://127.0.1.1:6386
Subscriber socket on localtest3 connected tcp://127.0.1.1:6388
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (-23.70696032985893, -197.00341197656513), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (0, 0)}
Node coordinates {'localtest1': (3, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (3, 0)}
Node coordinates {'localtest1': (5, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (5, 0)}
Node coordinates {'localtest1': (7, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (7, 0)}
Node coordinates {'localtest1': (9, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (9, 0)}
Node coordinates {'localtest1': (11, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (11, 0)}
Node coordinates {'localtest1': (13, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (13, 0)}
Node coordinates {'localtest1': (15, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (15, 0)}
Node coordinates {'localtest1': (17, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (17, 0)}
Node coordinates {'localtest1': (19, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (19, 0)}
Node coordinates {'localtest1': (21, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (21, 0)}
Node coordinates {'localtest1': (21, 0), 'localtest2': (164.39038497964964, 175.7075989455056), 'localtest3': (32.891029223579636, 68.625392595194), 'flag': (21, 0)}
```
