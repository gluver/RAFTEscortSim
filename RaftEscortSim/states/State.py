from RaftEscortSim.messages.VoteResponseRP import VoteRequestRP
from RaftEscortSim.messages.BaseMessage import BaseMessage
from RaftEscortSim.nodes.ServerNode import Node
from RaftEscortSim.messages.VoteRequestRQ import VoteRequestRQ

ELECTION_TIMEOUT=500
class State():
    '''
    Class Summary:
        Responsibale for behaviour logic of the nodes,while ServerNode class in charge of network config initializtion
    '''
    def __init__(self,node:Node,election_timeout=ELECTION_TIMEOUT):
        self.node=node
        self.election_timeout=election_timeout
    def persistent():
        '''
        Each server persists the following to stable storage
        synchronously before responding to RPCs:
        currentTerm
        latest term server has seen (initialized to 0
        on first boot)
        votedFor
        candidateId that received vote in current
        term (or null if none)
        log[]
        log entries
        '''
        pass

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
                (self.node.votedfor==None or self.node.vote_for==msg.c_id))
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
    def handle_log_request(self,msg):
        ''''''
        pass
    def handle_log_response(self,msg):
        ''''''
        pass
    def call_election(self):
        self.node.last_term=self.node.current_term
        self.node.current_term+=1
        self.node.change_state('Candidate')
        self.node.vote_for=self.node.node_id
        self.node.votes_received.append(self.node.node_id)
        if len(self.node.log)>0 :
            self.node.last_term=self.node.log[-1].term
            msg=VoteRequestRQ(self.node.node_id,self.node.current_term,
            len(self.node.log),self.node.last_term)
            self.node.queue.put(msg)
        #ToDo: Start election timer

    
