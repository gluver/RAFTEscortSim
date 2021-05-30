from RaftEscortSim.nodes.ServerNode import Node


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
    def handle_message(self,msg):
        if msg.type=="vote_request":
            self.handle_vote_request(msg)
        if msg.type=="apend_entries_request":
            pass
    def handle_vote_request(self,msg):
        pass
    def handle_append_entries_request(self,msg):
        pass
    def send_vote_request(self):
        pass
