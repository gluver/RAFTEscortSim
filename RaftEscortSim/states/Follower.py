from RaftEscortSim.nodes.ServerNode import Node # remove after 
import RaftEscortSim.states.State as State


class Follower(State.State):
    def __init__(self,node:Node,election_timeout=State.ELECTION_TIMEOUT):
        super().__init__(node)
        pass
    def handle_vote_request(self,msg):
        pass
    def handle_append_entries_request(self,msg):
        pass
    def send_vote_request(self):
        pass
    
if __name__=="__main__":
    f=Follower()
