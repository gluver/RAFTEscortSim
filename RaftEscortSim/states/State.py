from RaftEscortSim.messages.LogRP import LogRP
from RaftEscortSim.messages.LogRQ import LogRQ
from RaftEscortSim.messages.VoteResponseRP import VoteRequestRP
from RaftEscortSim.messages.BaseMessage import BaseMessage
# from RaftEscortSim.nodes.ServerNode import Node
from RaftEscortSim.messages.VoteRequestRQ import VoteRequestRQ
import time,random
ELECTION_TIMEOUT=1000 #ms
class State():
    '''
    Class Summary:
        Responsibale for behaviour logic of the nodes,while ServerNode class in charge of network config initializtion
    '''
    def __init__(self,node):
        self.node=node
        self.election_timeout=random.uniform(ELECTION_TIMEOUT,ELECTION_TIMEOUT*2)/1000
        

    def handle_message(self,msg:BaseMessage):
        if msg.type=='BaseMessage':
            print(f"Message from {msg.senderId} handled")
        if msg.type=='VoteRequestRQ':
            self.handle_vote_request(msg)
        if msg.type=='VoteRequestRP':
            self.handle_vote_response(msg)
        if msg.type=="LogRP":
            self.handle_log_response(msg)
        if msg.type=='LogRQ':
            self.handle_log_request(msg)

    def handle_vote_request(self,msg:VoteRequestRQ):
        my_logterm=self.node.log[-1].term
        log_ok=(msg.c_lastterm>my_logterm) or \
            (msg.c_lastterm==my_logterm and msg.c_loglen>=len(self.node.log))
        term_ok=(msg.c_term>self.node.current_term) or \
            (msg.c_term==self.node.current_term and \
                (self.node.vote_for==None or self.node.vote_for==msg.c_id))
        if log_ok and term_ok:
            self.node.current_term=msg.c_term
            if self.node.state_str !='Follower':
                self.node.change_state('Follower')
            self.node.vote_for=msg.c_id

            response=VoteRequestRP(self.node.node_id,self.node.current_term,True,msg.c_id)
        else:
            response=VoteRequestRP(self.node.node_id,self.node.current_term,False,msg.c_id)
        self.node.queue.put(response)
        
    def handle_vote_response(self,msg):
        ''''''
        pass
    def send_vote_request(self,msg):
        ''''''
        pass
    def handle_log_request(self, msg:LogRQ):
        print(f"{msg.f_id} handling {msg.type},node coordinates in last log:{msg.entries[-1].node_coordinates} from {msg.senderId}, ")
        if msg.f_id==self.node.node_id:
            if msg.l_term>self.node.current_term:
                self.node.current_term=msg.l_term
                self.node.vote_for=None
                if self.node.state_str !='Follower':
                    self.node.change_state('Follower')
                self.node.current_leader=msg.senderId 
            if msg.l_term==self.node.current_term and self.node.state_str=='Candidate':
                self.node.current_leader=msg.senderId
                self.node.change_state('Follower')
            logOk=(len(self.node.log)>=msg.log_len) and (msg.log_len==0 or msg.l_term==self.node.log[-1].term)
            if msg.l_term==self.node.current_term and logOk:
                self.append_entiries(msg.log_len,msg.l_commitlen,msg.entries)
                ack=msg.log_len+len(msg.entries)
                response=LogRP(self.node.node_id,self.node.current_term,ack,True)
            else:
                response=LogRP(self.node.node_id,self.node.current_term,0,False)
            self.node.queue.put(response)

    def handle_log_response(self,msg):
        ''''''
        pass
    def call_election(self):
        print(f"{self.node.node_id} calling election")
        self.node.last_term=self.node.current_term
        self.node.current_term+=1
        self.node.vote_for=self.node.node_id
        self.node.votes_received.append(self.node.node_id)
        if len(self.node.log)>0 :
            self.node.last_term=self.node.log[-1].term
            msg=VoteRequestRQ(self.node.node_id,self.node.current_term,
            len(self.node.log),self.node.last_term)
            self.node.queue.put(msg)
        if self.node.state_str=="Follower":
            self.node.change_state('Candidate')
        self.node.last_update=time.time()


    
