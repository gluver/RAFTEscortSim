from RaftEscortSim.log.Log import LogEntity
import os
import threading
import time
import random
import pickle
from typing import List
import zmq
import socket 
import yaml
from RaftEscortSim.states import Candidate,Follower,Leader
from RaftEscortSim.messages import BaseMessage,LogRP,LogRQ,VoteRequestRQ,VoteResponseRP
import queue

DICT_ROLE={0:'follower',1:'candidate',3:'leader'}
ELETION_TIMEOUT=150
LOG_DIR='./RAFTEscort.logc'
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
    def __init__(self,name,logdir=LOG_DIR,config_file=CONFIG_FILE) -> None:
        self.nodescoord=None ### store all nodes coords, coords inited by first leader
        with open(config_file,'r') as file:
            self.cluster_config=yaml.load(file, Loader=yaml.FullLoader)
        self.ip=self.get_host_ip()
        # self.port=self.cluster_config[self.ip]['port']
        # self.node_id=f'{self.ip}:{self.port}'###Todo:use ip:port as id
        self.queue=queue.Queue()
        self.node_id=name
        self.port=self.cluster_config[name]['port']
        self.current_term=0
        self.state=Follower.Follower(self) ### init as follower
        self.state_str="Follower"
        self.log:List[LogEntity]=[] ### Todo: Check if in disk_dir has presisted log
        init_entity=LogEntity(1)
        # init_entity=LogEntity(self.current_term)
        for n in self.cluster_config.keys():
            init_entity.node_coordinates[n]=(random.uniform(-200,200),random.uniform(-200,200))
        self.log.append(init_entity)
        self.election_timeout=random.randint(ELETION_TIMEOUT,ELETION_TIMEOUT*2)
        self.current_leader=None
        self.coordianter=None
        self.commit_length=0
        self.vote_for=None
        self.votes_received=[]
        self.last_term=None
        self.neighbours=self.get_neighbours()
        self.logdir=logdir
        if self.check_log_file_exist():### Find if there is a log file in current node for detecting preceeding crash
            self.recover()

        self.setup()

    def check_log_file_exist(self):
        return os.path.isfile(self.logdir)
    

    def get_host_ip(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def get_neighbours(self):
        return [n for n in self.cluster_config.items() if n[0]!=self.node_id]
  

    def setup(self):
        '''
        Summary:
            Setup connection with other server nodes in cluster
        '''
        class SubscriberThread(threading.Thread):
            def run(thread):
                context=zmq.Context()
                socket=context.socket(zmq.SUB)
                for neighbour_id,neighbour_info in self.neighbours:
                    socket.connect(f"tcp://{neighbour_info['ip']}:{neighbour_info['port']}")
                    print(f"Subscriber socket on {self.node_id} connected tcp://{neighbour_info['ip']}:{neighbour_info['port']}")
                socket.setsockopt(zmq.SUBSCRIBE,b'')
                while True:
                    message=socket.recv_pyobj()
                    if message:
                        self.state.handle_message(message)
                        # print(f'{self.node_id} recived {type(message)}') ##
                    else:
                        self.housekeeping()
                    ##Todo invoke state message handle message
                    
                print(f"{self.node_id}")
        class PublisherThread(threading.Thread):
            def run(thread):
                context=zmq.Context()
                socket=context.socket(zmq.PUB)
                socket.bind(f"tcp://{self.ip}:{self.port}")
                print(f"Publisher socket on {self.node_id} binded tcp://{self.ip}:{self.port}")
                while True:
                    time.sleep(1)
                    # self.queue.put(BaseMessage.BaseMessage(self.node_id))
                    if self.queue.qsize() !=0:
                        message= self.queue.get()##Todo: get messenge or rcp from state 
                        if message:
                            # print(f'{self.node_id} sending msg ....')
                            socket.send_pyobj(message)
                            
                       
                    
        self.subscriber_thread=SubscriberThread()
        self.publisher_thread=PublisherThread()
        self.subscriber_thread.isDaemon=True
        self.subscriber_thread.start()
        self.publisher_thread.isDaemon=True
        self.publisher_thread.start()
        # self.publisher_thread.join()
        # self.subscriber_thread.join()

    def recover(self):###ToDo Define Object for presist,figure out when to dump the Object file 
        '''
        load logfile: in logfile : currentTerm, votedFor ,log, and commitLength
        '''
        with open(self.logdir,'rb') as file:
            data=pickle.load(file)
            self.current_term=data.current_term
            self.vote_for=data.vote_for
            self.log=data.log
            self.commit_length=data.commit_length

    def housekeeping(self):
        now=time.time()
        print(now)
    def change_state(self,target_state):
        if target_state=='Follower':
            self.state_str='Follower'
            self.state=Follower.Follower(self)
        elif target_state=='Candidate':
            self.state_str='Candidate'
            self.state=Candidate.Candidate(self)
        elif target_state=='Leader':
            self.state=Leader.Leader(self)
            self.state_str='Leader'
if __name__=="__main__":
    ###Test code
    # with open(CONFIG_FILE,'r') as file:
    #     a=yaml.load(file, Loader=yaml.FullLoader)
        # print(a,a.items())
    node=Node('localtest1')
    node1=Node('localtest2')
    node3=Node('localtest3')
    node.state.call_election()
   