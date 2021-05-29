import os
import socket
import threading
import time
import random
import pickle
import zmq
from RaftEscortSim.messager import BasicMessager
from RaftEscortSim.states import Candidate,Follower,Leader

DICT_ROLE={0:'follower',1:'candidate',3:'leader'}
ELETION_TIMEOUT=150
LOG_DIR=os.path.abspath('.')
class Node():
    '''
    ClassSummary:
        1.Nodes initialized on random coordinates
        2.There is a flag at initial point (0, 0)
        3.One of the nodes should get the flag from (0, 0) to (100, 0) making 1 point step at a time
        4.Others should escort it keeping it in the center. If leading node is lost, one of the escorting should get to the last point of coordinator node was in and continue the trip.
    ToDo:
        1.Node coordinate init randomly ***1.How to keep flag in center? move the nodes(introduce node coordinate)? May followers teleport to a proper place to form a regular polygon that centers the leading node(which carrys flag)?
        *** ***2.How can we find the 'proper place' for escorting Nodes 
        2.Flag coordinate init as (0, 0)
        3.Load Cluster Config {NodeAdresses} ***Can be done in Messenger class***
        4.Node init as follower, init election timeout randomly ***The range of timeout [T, 2T], T>> communication delay
        5.Node timeout triggered, vote for itself, broadcast ElectionRPC to other Nodes(in parallel) ***How to get to know Cluster Cofig.*** 
        If timeout not triggered, keep behaviour as a follower,only vote for the first arrived ElectionRPC
            5.1 Node become leader, run leader method
                leader behaviour
            5.2 Node remain follower, run follower method
                follower behaviour
            5.3 Split vote, Re Election
                candidate behaviour
        6.What does an entity in log looks like?
    Definiation:
        log:
        CONFIG_FILE: File stores node_id 
    '''
    def __init__(self,node_id,logdir=LOG_DIR) -> None:
        self.nodescoord=None ### store all nodes coords, coords inited in configuration file
        self.node_id=node_id
        self.current_term=0
        self.state='follower' ### init as follower
        self.log=[] ### Todo: Check if in disk_dir has presisted log
        self.election_timeout=random.randint(ELETION_TIMEOUT,ELETION_TIMEOUT*2)
        self.coordianter=None
        self.commit_length=0
        self.vote_for=None
    def setup(self,port):
        '''
        Summary:
            Setup connection with other server nodes in cluster
        '''
        
        pass
    def go_online(self):
        pass
node=Node()