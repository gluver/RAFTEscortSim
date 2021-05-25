# RAFTEscortSim
This project implemented “Escort simulator” using Raft consensus algorithm.

Assumptions:

There are n nodes in 2D (n ≥ 3) (nodes initialized on random coordinates)
There is a flag at initial point (0, 0)
One of the nodes should get the flag from (0, 0) to (100, 0) making 1 point step at a time

Others should escort it keeping it in the center. If leading node is lost, one of the escorting should get to the last point of coordinator node was in and continue the trip.