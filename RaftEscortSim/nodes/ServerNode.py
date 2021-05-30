import os
import threading
import time
import random
import pickle
from typing import ContextManager
import zmq
import socket 
import yaml
from RaftEscortSim.states import Candidate,Follower,Leader

DICT_ROLE={0:'follower',1:'candidate',3:'leader'}
ELETION_TIMEOUT=150
LOG_DIR=os.path.abspath('.')
CONFIG_FILE=os.path.join('.','ClusterConfig.yaml')###***Todo: Should configure out path
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
    def __init__(self,logdir=LOG_DIR,config_file=CONFIG_FILE) -> None:
        self.nodescoord=None ### store all nodes coords, coords inited by first leader
        with open(config_file,'r') as file:
            self.cluster_config=yaml.load(file, Loader=yaml.FullLoader)
        self.ip=self.get_host_ip()
        self.port=self.cluster_config[self.ip]['port']
        self.node_id=f'{self.ip}:{self.port}'###Todo:use ip:port as id
        self.current_term=0
        self.state='follower' ### init as follower
        self.log=[] ### Todo: Check if in disk_dir has presisted log
        self.election_timeout=random.randint(ELETION_TIMEOUT,ELETION_TIMEOUT*2)
        self.coordianter=None
        self.commit_length=0
        self.vote_for=None
        self.neighbours=self.get_neighbours()
        self.setup()

    def get_host_ip(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def get_neighbours(self):
        return [n for n in self.cluster_config.items() if n[0]!=self.get_host_ip()]
  

    def setup(self):
        '''
        Summary:
            Setup connection with other server nodes in cluster
        '''
        class SubscriberThread(threading.Thread):
            def run(thread):
                context=zmq.Context()
                socket=context.socket(zmq.SUB)
                for neighbour_ip,neighbour_info in self.neighbours:
                    socket.connect(f"tcp://{neighbour_ip}:{neighbour_info['port']}")
                    print(f"Subscriber socket coonected tcp://{neighbour_ip}:{neighbour_info['port']}")
                while True:
                    message=socket.recv()
                    ##Todo invoke state message handle message
        class PublisherThread(threading.Thread):
            def run(thread):
                context=zmq.Context()
                socket=context.socket(zmq.PUB)
                socket.bind(f"tcp://{self.ip}:{self.port}")
                print(f"Publisher socket binded tcp://{self.ip}:{self.port}")
                while True:
                    message=None ##Todo: get message or rcp from state 
                    if message:
                        socket.send(message)

        self.subscriber_thread=SubscriberThread()
        self.publish_thread=PublisherThread()
        self.subscriber_thread.setDaemon(True)
        self.publish_thread.setDaemon(True)
        self.subscriber_thread.start()
        self.publish_thread.start()

 

if __name__=="__main__":
    ###Test code
    # with open(CONFIG_FILE,'r') as file:
    #     print(yaml.load(file, Loader=yaml.FullLoader) )
    node=Node()
    ip=node.get_host_ip()
    print(node.get_neighbours(),node.node_id)
    print(node.get_host_ip())